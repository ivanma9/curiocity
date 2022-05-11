import json
import sys

data = json.load(open('busstop.geojson', 'r'))
bus_stops_list = []
for item in data['features']:
    #print(bus['geometry'])
    bus_stops_list.append(item['geometry'])

#with open('bus_stops.json', 'w') as f:
    #json.dump(bus_stops_list, f)

#print(bus_stops_list)

sys.stdout = open('buslist.js', 'w')

bus_stops_json = json.dumps(bus_stops_list)

print("var busjsonstr = '{}' ".format(bus_stops_json))
