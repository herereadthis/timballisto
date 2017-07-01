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

def string_in_string(sub_string, parent_string):
    """determine if one string is inside another."""
    return sub_string.lower() in parent_string.lower()


def get_city_id():
    """Filter the list of cities to grab ID from city name."""
    print('Loading city list...')
    data = load_city_json()
    city = input('What is the closest city to the place to where you are' +
                 'travelling?')
    city_id = False
    # list comprehension
    possible_cities = [d for d in data if string_in_string(city, d['name'])]

    pprint(possible_cities)

    for item in possible_cities:
        question = 'Is this in %s? y/n' % (item['country'])
        answer = input(question)
        if answer == 'y':
            city_id = item['id']
            break

    if not city_id:
        print('Sorry, that location is not available.')

    return city_id


def get_weather_data(city_id):
    """Get the weather forecast given a city ID."""
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=%s'
    api_url = (url) % (city_id, open_weather_map_key)

    return api_url


def forecast():
    """Run the main thing."""
    city_id = get_city_id()

    if city_id != False:
        url = get_weather_data(city_id)
        print(url)
    else:
        print('No Luck today.')


if __name__ == '__main__':
    forecast()

