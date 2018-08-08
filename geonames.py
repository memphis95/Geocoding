# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:50:20 2018

@author: Bugs
"""
import pandas as pd
import requests
import csv
import xml.etree.ElementTree as ET

#Enter your own GEONAMES USERNAME here.
username = None

output_filename = "output.csv"
input_filename = "dataset.csv"
address_column_name = "StreetAddress"

data = pd.read_csv(input_filename, encoding='utf8')
addresses = data[address_column_name].tolist()
addresses = (data[address_column_name] + ',' + data['City'] ).tolist()

def func(address, username):
    geocode_url = "http://api.geonames.org/geoCodeAddress?q={}".format(address)
    geocode_url = geocode_url + "&username={}".format(username)
    results = requests.get(geocode_url)
    msg = results.content
    tree = ET.fromstring(msg)
    roww = []
    #hno = str(tree.findtext('.//houseNumber'))
    locality = str(tree.findtext('.//locality'))
    street = str(tree.findtext('.//street'))
    addr =  street +", "+ locality
    print(addr+"\n")
    lat = tree.findtext('.//lat')
    long = tree.findtext('.//lng')
    roww.append(addr)
    roww.append(lat)
    roww.append(long)
    csvwriter.writerow(roww)

output = open(output_filename, 'w', newline='')
csvwriter = csv.writer(output)
rowheader = ['Address', 'Latitude', 'Longitude']
csvwriter.writerow(rowheader)

for address in addresses:
    func(address, username)

output.close()