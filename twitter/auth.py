"""Grab Twitter Keys to authenticate."""

import json

with open('./../../secret.json') as json_data:
    data = json.load(json_data)['twitter']
    consumer_key = data['consumerKey']
    consumer_secret = data['consumerSecret']
    access_token = data['accessToken']
    access_token_secret = data['accessTokenSecret']