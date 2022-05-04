from operator import is_
from re import search
import requests
import json
import os
from parse import titles

from dotenv import load_dotenv
load_dotenv()


# Define my API Key, My Endpoint, and My Headerg
API_KEY = os.environ.get("YELP_API_KEY")
SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
CATEGORY_ENDPOINT = 'https://api.yelp.com/v3/categories'
BUSINESS_DETAILS_ENDPOINT = 'https://api.yelp.com/v3/businesses'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}


# Server endpoint
HEROKU_SERVER = 'http://localhost:8080/insertbusinesses'#'https://enigmatic-brook-87129.herokuapp.com'

# Define my parameters of the search
LA_COUNTY_CITIES = [
"Agoura Hills",
"Alhambra",
"Arcadia",
"Artesia",
"Avalon",
"Azusa",
"Baldwin Park",
"Bell",
"Bell Gardens",
"Bellflower",
"Beverly Hills",
"Bradbury",
"Burbank",
"Calabasas",
"Carson",
"Cerritos",
"Claremont",
"Commerce",
"Compton",
"Covina",
"Cudahy",
"Culver City",
"Diamond Bar",
"Downey",
"Duarte",
"El Monte",
"El Segundo",
"Gardena",
"Glendale",
"Glendora",
"Hawaiian Gardens",
"Hawthorne",
"Hermosa Beach",
"Hidden Hills",
"Huntington Park",
"Industry",
"Inglewood",
"Irwindale",
"La Cañada Flintridge",
"La Habra Heights",
"La Mirada",
"La Puente",
"La Verne",
"Lakewood",
"Lancaster",
"Lawndale",
"Lomita",
"Long Beach",
"Los Angeles",
"Lynwood",
"Malibu",
"Manhattan Beach",
"Maywood",
"Monrovia",
"Montebello",
"Monterey Park",
"Norwalk",
"Palmdale",
"Palos Verdes Estates",
"Paramount",
"Pasadena",
"Pico Rivera",
"Pomona",
"Rancho Palos Verdes",
"Redondo Beach",
"Rolling Hills",
"Rolling Hills Estates",
"Rosemead",
"San Dimas",
"San Fernando",
"San Gabriel",
"San Marino",
"Santa Clarita",
"Santa Fe Springs",
"Santa Monica",
"Sierra Madre",
"Signal Hill",
"South El Monte",
"South Gate",
"South Pasadena",
"Temple City",
"Torrance",
"Vernon",
"Walnut",
"West Covina",
"West Hollywood",
"Westlake Village",
"Whittier",
    ]

PARAMETERS_LOS_ANGELES = []

# fills out the parameters object array for LA county
for elem in LA_COUNTY_CITIES:
    PARAMETERS_LOS_ANGELES.append({
        'location': elem,
        'radius': 40000
    })

# This function gets parent aliases from the base alias list 
# Returns list of tags to be added to the business
def getTagsFromAliases(aliases):
    tags_set = set()
    for alias, title in aliases:
        # hit Yelp Category api to get parent aliases
        category_url = CATEGORY_ENDPOINT + '/' + alias
        category_request = requests.get(
                        url =  category_url,
                        headers = HEADERS
                        ).json()
        
        for parent_alias in category_request["category"]["parent_aliases"]:
            if parent_alias in titles:
                parent_tag_title = titles[parent_alias] 
                tags_set.add(parent_tag_title)

        # Add title to tags_list
        if alias in titles:
            tags_set.add(title)

    # return list of the tags set
    return list(tags_set)

def get_business_details(id):
    details_url = BUSINESS_DETAILS_ENDPOINT + '/' + id
    details_request = requests.get(
                    url =  details_url,
                    headers = HEADERS
                    ).json()
    return details_request

# This function constructs a business from the yelp format to the curiocity format
def construct_business(search_response_body):
    
    # Return business
    curiocity_businesses = []

    res_search_queries = search_response_body["res"]

    for city_query in res_search_queries:
        businesses = city_query["businesses"]
        # for each business
        for business in businesses:           

            # Gathering aliases from the categories 
            categories = business.get("categories")
            if (categories):
                # each aliases is one array of aliases for one business
                aliases = []
                for category in categories:
                    my_tuple = (category["alias"], category["title"])
                    aliases.append(my_tuple)

                # this is the tags list we want to add to the business
                tags_list = getTagsFromAliases(aliases)

                #print(getTagsFromAliases(aliases))

            # grab data from details of business using yelp Business Details API
            yelp_id = business.get("id")
            details_response = get_business_details(yelp_id)
            yelp_photos = details_response.get("photos")
            hours = details_response.get("hours")
            special_hours = details_response.get("special_hours")
            is_closed = details_response.get("is_closed")

            # TODO: new JSON body of location/business
            coordinates = dict(reversed(list(business.get("coordinates").items())))
            curiocity_business_json = json.dumps({
                "name": business.get("name"),
                "phone": business.get("phone"),
                "price": business.get("price"),
                "photos": yelp_photos,
                "location": business.get("location"),
                "coordinates": coordinates,
                "hours": hours,
                "special_hours": special_hours,
                "is_closed": is_closed,
                "tags": tags_list
            })

            # Add json to business array
            curiocity_businesses.append(curiocity_business_json)

    return curiocity_businesses

# function to get JSON object of aggregated queries of businesses in all the cities of LA county
def getYelpAPI_LA():
    # Make a request to the Yelp API
    response_array = []
    for cityParameter in PARAMETERS_LOS_ANGELES:
        response_array.append(
            requests.get(
                    url = SEARCH_ENDPOINT,
                    params = cityParameter,
                    headers = HEADERS
                    ).json())
    
    response = {
        "res": response_array
    }

    search_response_body = json.loads(json.dumps(response))

    # Create an updated json from the yelp search with what curiocity wants
    updated_businesses_array = construct_business(search_response_body)
    updated_businesses_json = {
        "res": updated_businesses_array
    }
    return json.loads(json.dumps(updated_businesses_json))
print(getYelpAPI_LA())
# Open categories

# Find parent categories for 
# ONE business
# aliases [(alias, title)]



f = requests.post(HEROKU_SERVER, json=getYelpAPI_LA())
