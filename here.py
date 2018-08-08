# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:50:20 2018

@author: Bugs
"""
import pandas as pd
import requests
import csv
import xml.etree.ElementTree as ET

#Enter your HERE APP ID and HERE APP CODE here.
HERE_APP_ID = None
HERE_APP_CODE = None

output_filename = "output.csv"
input_filename = "dataset.csv"
address_column_name = "StreetAddress"

data = pd.read_csv(input_filename, encoding='utf8')
addresses = data[address_column_name].tolist()
addresses = (data[address_column_name] + ',' + data['City'] + ',United States of America').tolist()

def func(address):
    geocode_url = "https://geocoder.cit.api.here.com/6.2/geocode.xml?searchtext={}".format(address)
    geocode_url = geocode_url + "&app_id={}".format(HERE_APP_ID) + "&app_code={}".format(HERE_APP_CODE)
    results = requests.get(geocode_url)
    msg = results.content
    tree = ET.fromstring(msg)
    roww = []
    addr = tree.findtext('.//Label')
    lat = tree.findtext('.//DisplayPosition/Latitude')
    long = tree.findtext('.//DisplayPosition/Longitude')
    roww.append(addr)
    roww.append(lat)
    roww.append(long)
    csvwriter.writerow(roww)

output = open(output_filename, 'w', newline='')
csvwriter = csv.writer(output)
rowheader = ['Address', 'Latitude', 'Longitude']
csvwriter.writerow(rowheader)

for address in addresses:
    func(address)

output.close()