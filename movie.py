#!/usr/bin/python3

import sys
import requests
import json
import os

url = "http://www.omdbapi.com/"

#get OMDb API Key: set a default key in case not been set
mykey=os.environ.get('MY_KEY')
if mykey == None:
    mykey="5394c9bc"

#Get the movie name 
m_name = sys.argv[1]
if len(m_name) == 0 :
    print ("Movie name missing")
    sys.exit()

querystring = {"apikey":mykey, "t":m_name}

headers = {
    'cache-control': 'no-cache',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_text = json.loads(response.text)

#verify if movie exists
if json_text['Response'] == 'True' :
    ratings = json_text['Ratings']
    if (len(ratings) > 0) :
        #verify if Rotten Tomatoes rating exist
        for rate in ratings:
            if (rate['Source'] == 'Rotten Tomatoes'):
                print("\"{}\" Rotten Tomatoes rating is: {}".format(m_name, rate['Value']))
                break
        else:
            print("\"{}\" don't have \'Rotten Tomatoes\' rating, but it has \'{}\' value which is: {}".format(m_name, rate['Source'], rate['Value']))
    else :
        print("\"{}\" have no Ratings available".format(m_name))
else :
    print("\"{}\" {}".format(m_name, json_text['Error']))

