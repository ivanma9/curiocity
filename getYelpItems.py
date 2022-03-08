from re import search
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


# Define my API Key, My Endpoint, and My Headerg
API_KEY = os.environ.get("YELP_API_KEY")
SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
CATEGORY_ENDPOINT = 'https://api.yelp.com/v3/categories'
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
for elem in LA_COUNTY_CITIES[1:2]:
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
            # TODO: findTitle in tag - kunal parent_alias is key
            parent_tag_title = parent_alias
            

            tags_set.add(parent_tag_title)

        # Add title to tags_list
        tags_set.add(title)

    return list(tags_set)



# This function gets list of alias tuples
def getCategories(search_response_body):
    search_response_dict = json.loads(json.dumps(search_response_body))

    res = search_response_body["res"]

    overall_aliases = []

    for item in res:
        businesses = item["businesses"]
        # for each business
        for business in businesses:            
            categories = business["categories"]
            # each aliases is one array of aliases for one business
            aliases = []
            for category in categories:
                my_tuple = (category["alias"], category["title"])
                aliases.append(my_tuple)

            # this is the tags list we want to add to the business
            tags_list = getTagsFromAliases(aliases)

            # print(getTagsFromAliases(aliases))

            # TODO: new JSON body of location/business
            curiocity_business = json.dumps({
                "name": business["name"],
                "phone": business["phone"],
                "price": business["price"],
                "image_url": business["image_url"],
                "location": business["location"],
                "coordinates": business["coordinates"],
                "tags": tags_list
            })

            overall_aliases.append(aliases)

    return overall_aliases

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

    aliases = getCategories(search_response_body)
    
    return aliases



# Open categories

(getYelpAPI_LA())

# Find parent categories for 
# ONE business
# aliases [(alias, title)]



# f = requests.post(HEROKU_SERVER, json=getYelpAPI_LA())
