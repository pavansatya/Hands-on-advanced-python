# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snow_days= list(filter(lambda x: x['snow'] > 0.0, weatherdata))
snow_days

# TODO: pretty-print the resulting data set
pprint.pp(snow_days)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summer_rainy_days = []

    for day in weatherdata:
        if '-01-'and '-08-' in day['date'] and day["prcp"] > 1.0:
            summer_rainy_days.append(day['date'])

    return summer_rainy_days

summer_rainy_days = is_summer_rain_day(weatherdata)
summer_rainy_days