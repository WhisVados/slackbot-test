import os
import googlemaps
import pdb
import requests
import time
import json
#API Key - store in env variable later
maps_key = 'AIzaSyAljglOaoVy3JSrmnIrGq2saSIxdXOV_ks'

def timezone(location):
    endpoint = 'https://maps.googleapis.com/maps/api/timezone/json?'
    gm = googlemaps.Client(maps_key)
    timestamp = time.time()
    #query geocode data based on location and stores longitude and latitude to respective variable
    geocode_result = gm.geocode('Vancouver')[0]
    #location = geocode_result['geometry']['location']
    latitude = geocode_result['geometry']['location']['lat']
    longitude = geocode_result['geometry']['location']['lng']

    #website = 'https://maps.googleapis.com/maps/api/timezone/json?location=38.908133,-77.047119&timestamp=1458000000&key=AIzaSyAljglOaoVy3JSrmnIrGq2saSIxdXOV_ks'
    website = endpoint + 'location=' + str(latitude) + ',' + str(longitude) + '&timestamp=' + str(timestamp) + '&key=' + maps_key
    resp = requests.get(website)
    print(resp.json())

location = 'Vancouver'
timezone(location)
