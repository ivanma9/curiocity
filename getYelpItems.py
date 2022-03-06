from re import search
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


# Define my API Key, My Endpoint, and My Headerg
API_KEY = os.environ.get("YELP_API_KEY")
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
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

#function to get list of alias tuples
def getCategories(search_response_body):
    x = json.dumps(search_response_body)

    y = json.loads(x)

    # print(y["res"][1])

    res = y["res"]

    aliases = []

    for item in res:
        businesses = item["businesses"]
        # print(businesses)
        for business in businesses:
            # print(business["categories"])
            categories = business["categories"]
            #each new_list is one array of aliases which is what you want
            new_list = []
            for category in categories:
                # print(category)
                my_tuple = (category["alias"], category["title"])
                # print(my_tuple)
                new_list.append(my_tuple)
            aliases.append(new_list)


    for item in aliases:
        print(item)

    return aliases

# function to get JSON object of aggregated queries of businesses in all the cities of LA county
def getYelpAPI_LA():
    # Make a request to the Yelp API
    response_array = []
    for cityParameter in PARAMETERS_LOS_ANGELES:
        response_array.append(
            requests.get(
                    url = ENDPOINT,
                    params = cityParameter,
                    headers = HEADERS
                    ).json())
    
    response = {
        "res": response_array
    }

    search_response_body = json.loads(json.dumps(response))

    aliases = getCategories(search_response_body)

    
    

    print(aliases)
    return aliases


getYelpAPI_LA()

# f = requests.post(HEROKU_SERVER, json=getYelpAPI_LA())
