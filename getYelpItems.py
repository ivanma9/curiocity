#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


# Define my API Key, My Endpoint, and My Header
API_KEY = os.environ.get("YELP_API_KEY")
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}

# Server endpoint
HEROKU_SERVER = "localhost:8080/insertbusinesses"#"https://enigmatic-brook-87129.herokuapp.com"

# Define my parameters of the search
PARAMETERS_LOS_ANGELES = {
        'location': 'Los Angeles',
        'radius': 40000
    }
PARAMETERS_SAN_DIEGO = {
        'location': 'San Diego',
        'radius': 40000
    }
PARAMETERS_SAN_FRANCISCO = {
        'location': 'San Francisco',
        'radius': 40000
    }
PARAMETERS_LAS_VEGAS = {
        'location': 'Las Vegas',
        'radius': 40000
    }
PARAMETERS_ORANGE_COUNTY = {
        'location': 'Irvine',
        'radius': 40000
    }


def getYelpAPI():
    # Make a request to the Yelp API
    response_la = requests.get(
                                url = ENDPOINT,
                                params = PARAMETERS_LOS_ANGELES,
                                headers = HEADERS
                                )
    response_sd = requests.get(
                                url = ENDPOINT,
                                params = PARAMETERS_SAN_DIEGO,
                                headers = HEADERS
                                )
    response_sf = requests.get(
                                url = ENDPOINT,
                                params = PARAMETERS_SAN_FRANCISCO,
                                headers = HEADERS
                                )
    response_lv = requests.get(
                                url = ENDPOINT,
                                params = PARAMETERS_LOS_ANGELES,
                                headers = HEADERS
                                )
    response_oc = requests.get(
                                url = ENDPOINT,
                                params = PARAMETERS_ORANGE_COUNTY,
                                headers = HEADERS
                                )
    response_array = [
        response_la.json(), 
        response_sd.json(), 
        response_sf.json(), 
        response_lv.json(), 
        response_oc.json()
        ]
    response = {
        "res": response_array
    }
    return json.dumps(response)


requests.post(HEROKU_SERVER, json=getYelpAPI())

# print((getYelpAPI()))
# for i in getYelpAPI():
#     print(json.dumps(i))

# print the response
# print(json.dumps(business_data, indent = 3))