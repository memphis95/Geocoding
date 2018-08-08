# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:50:20 2018

@author: Bugs
"""
import pandas as pd
import requests
import csv
import xml.etree.ElementTree as ET

output_filename = 'output.csv'
input_filename = "dataset.csv"
address_column_name = "StreetAddress"

data = pd.read_csv(input_filename, encoding='utf8')
addresses = data[address_column_name].tolist()
addresses = (data[address_column_name] + ',' + data['City'] ).tolist()

def func(address):
    geocode_url = "https://www.geocode.farm/v3/xml/forward/?addr={}".format(address)
    geocode_url = geocode_url + "&country=us&lang=en&count=1"
    results = requests.get(geocode_url)
    msg = results.content
    tree = ET.fromstring(msg)
    roww = []
    addr = str(tree.findtext('.//formatted_address'))
    print(addr+"\n")
    accuracy = tree.findtext('.//accuracy')
    lat = tree.findtext('.//COORDINATES/latitude')
    long = tree.findtext('.//COORDINATES/longitude')
    roww.append(addr)
    roww.append(accuracy)
    roww.append(lat)
    roww.append(long)
    csvwriter.writerow(roww)

output = open(output_filename, 'w', newline='')
csvwriter = csv.writer(output)
rowheader = ['Address', 'Accuracy','Latitude', 'Longitude']
csvwriter.writerow(rowheader)

for address in addresses:
    func(address)

output.close()