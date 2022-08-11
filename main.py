#!/bin/python

import sys
import json
from math import radians, sin, cos, sqrt, asin

from more_itertools import first

population_limit = int(sys.argv[1]) # taking population limit as command line argument
dataset = "data.json"

# function to find distance between two coordinates
def find_dist(latlng_1, latlng_2):
    lat1, lon1 = radians(latlng_1[0][0]), radians(latlng_1[0][1])
    lat2, lon2 = radians(latlng_2[0][0]), radians(latlng_2[0][1])
    d = 2*6371*asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1)
                    * cos(lat2)*sin((lon2-lon1)/2)**2))

    return round(d, 2)


with open(dataset, 'r') as f:  # Reading the dataset file
    countries = json.load(f)

first_20 = {}  # Dictionary to store the top 20 countries by population which match our criteria
currency_index = {}  # histogram of how many countries use a currency

for country in countries:  # making a histogram of the how many countries use a currency
    for currency in country['currencies']:
        currency_index[currency['code']] = currency_index.get(
            currency['code'], 0) + 1

for country in countries:
    # checking if a country's population is above our limit
    if country['population'] >= population_limit:
        for currency in country['currencies']:
            # checking if the country has at least one currency exclusive to them
            if currency_index[currency['code']] == 1:
                first_20[country['alpha3Code']] = []
                first_20[country['alpha3Code']].append(country['latlng'])
                first_20[country['alpha3Code']].append(country['population'])

                break

# filtering out top 20 countries by population
first_20 = dict(sorted(first_20.items(), key=lambda x: x[1][1])[:20])


# Calculating the distance between every country
total_dist = 0
keys = list(first_20.keys())
for i in range(len(first_20)):
    for j in range(i+1, len(first_20)):
        total_dist += find_dist(first_20[keys[i]], first_20[keys[j]])

# Rounding off total distance to 2 decimal points
total_dist = round(total_dist, 2)

print(total_dist)