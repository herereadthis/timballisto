"""Use OpenWeatherMap to do weather forecasting."""

from requests import get
from datetime import datetime, timedelta
import json
from pprint import pprint
from auth import (
    open_weather_map_key
)


def load_city_json():
    """Parse the city list JSON into a list."""
    with open('../downloads/city.list.json') as data_file:
        return json.load(data_file)


def get_city_id():
    """Filter the list of cities to grab ID from city name."""
    data = load_city_json()
    city = input('What is the closest city to the place to where you are' +
                 'travelling?')
    city_id = False
    # list comprehension
    possible_cities = [d for d in data if d['name'] == city]

    pprint(possible_cities)

    for item in possible_cities:
        answer = input('Is this in ' + item['country'] + '? y/n')
        if answer == 'y':
            city_id = item['id']
            break

    if not city_id:
        print('Sorry, that location is not available.')
        exit()

    return city_id
