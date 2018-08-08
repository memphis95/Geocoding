# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:28:23 2018

@author: Bugs
"""
import csv
import pandas as pd
from math import radians, cos, sin, asin, sqrt

data = pd.read_csv('output-all.csv')
data.fillna(0, inplace=True)
goog_lat = data['Google_lat'].tolist()
goog_long = data['Google_long'].tolist()
here_lat = data['Here_lat'].tolist()
here_long = data['Here_long'].tolist()
tamu_lat = data['Tamu_lat'].tolist()
tamu_long = data['Tamu_long'].tolist()
mapl_lat = data['Maplarge_lat'].tolist()
mapl_long = data['Maplarge_long'].tolist()
uscen_lat = data['Uscensus_long'].tolist()
uscen_long = data['Uscensus_lat'].tolist()
geo_lat = data['Geonames_lat'].tolist()
geo_long = data['Geonames_long'].tolist()

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371000 # Radius of earth in kilometers
    if(lat1==0 or lat2==0):
        return 0
    return c * r

output = open('haversine3', 'w', newline='')
csvwriter = csv.writer(output)
rowheader = ['1', '2', '3', '4', '5']
csvwriter.writerow(rowheader)

for i in range(1000):
    diff1 = haversine(goog_long[i], goog_lat[i], here_long[i], here_lat[i])
    diff2 = haversine(goog_long[i], goog_lat[i], tamu_long[i], tamu_lat[i])
    diff3 = haversine(goog_long[i], goog_lat[i], mapl_long[i], mapl_lat[i])
    diff4 = haversine(goog_long[i], goog_lat[i], uscen_long[i], uscen_lat[i])
    diff5 = haversine(goog_long[i], goog_lat[i], geo_long[i], geo_lat[i])
    row = []
    row.append(diff1)
    row.append(diff2)
    row.append(diff3)
    row.append(diff4)
    row.append(diff5)
    csvwriter.writerow(row)
    #print(diff)
    
output.close()

