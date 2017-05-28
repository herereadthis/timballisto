# Python HTTP requests
from requests import get
import json
# The pprint module provides a capability to “pretty-print” arbitrary Python data
# structures, tutorial at: https://docs.python.org/3/library/pprint.html
from pprint import pprint

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

# Use get from request module: fetch data and translate into Python dictionaries
# using the json module
stations = get(url).json()['items']
