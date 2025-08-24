"""Grab OpenWeatherMap Keys to authenticate."""

import json

with open('./../../secret.json') as json_data:
    data = json.load(json_data)['openWeatherMap']
    open_weather_map_key = data['key']
