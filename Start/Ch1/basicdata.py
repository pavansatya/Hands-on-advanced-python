# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmest_day = max(weatherdata, key=lambda x:x['tmax'])
print("The warmest day is {} with {} degrees".format(warmest_day['date'], warmest_day['tmax']))

# TODO: What was the coldest day in the data set?
coldest_day = min(weatherdata, key=lambda x:x['tmin'])
print("The coldest day is {} with {} degrees".format(coldest_day['date'], coldest_day['tmin']))


# TODO: How many days had snowfall?
count = 0
for day in weatherdata:
    if day['snow'] > 0.0:
        count = count + 1

print(count)        
