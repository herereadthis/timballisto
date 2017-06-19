"""Use OpenWeatherMap to do weather forecasting."""

from requests import get
from datetime import datetime, timedelta
import json
from pprint import pprint
from auth import (
    open_weather_map_key as owm_key
)

def load_city_json():
    with open('../downloads/city.list.json') as data_file:    
        return json.load(data_file)


def get_city_id():
    data = load_city_json()
    city = input('Which is the closest city to the place you are travelling to?' )
    city_id = False
    # list comprehension
    possible_cities = [d for d in data if d['name'] == city]

    pprint(possible_cities)

    for item in possible_cities:
        answer = input('Is this in '+ item['country'] + '? y/n')
        if answer == 'y':
            city_id = item['id']
            break

    if not city_id:
        print('Sorry, that location is not available.')
        exit()

    return city_id

def get_weather_data(city_id):
    """Get the weather forecast given a city ID."""
    url = 'http://api.openweathermap.org/'
    api_url = '%s/data/2.5/forecast?id=%s&APPID=%s' % (url, city_id, owm_key)
    weather_data = get(api_url)

    return weather_data.json()
