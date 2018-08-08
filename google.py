# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:50:20 2018

@author: Bugs
"""
import pandas as pd
import requests

#Enter your own GOOGLE MAPS API KEY here.
API_KEY = None

output_filename = "output.csv"
input_filename = "dataset.csv"
address_column_name = "StreetAddress"

data = pd.read_csv(input_filename, encoding='utf8')
addresses = data[address_column_name].tolist()
addresses = (data[address_column_name] + ',' + data['City'] + ',United States of America').tolist()

def get_google_results(address, api_key=None):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    if api_key is not None:
        geocode_url = geocode_url + "&key={}".format(api_key)
    results = requests.get(geocode_url)
    results = results.json()
    if len(results['results']) == 0:
        output = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:    
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components') 
                                  if 'postal_code' in x.get('types')])
        }    
    output['input_string'] = address
    output['number_of_results'] = len(results['results'])
    output['status'] = results.get('status')
    output['response'] = results
    return output

results = []
for address in addresses:
    geocode_result = get_google_results(address)
    results.append(geocode_result)
    
pd.DataFrame(results).to_csv(output_filename, encoding='utf8')

    