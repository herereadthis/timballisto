# https://www.raspberrypi.org/learning/graphing-the-weather/worksheet/

# Python HTTP requests
from requests import get
from pprint import pprint
# pyplot rovides a MATLAB-like plotting framework.
import matplotlib.pyplot as plt
# The dateutil module provides extensions to the standard datetime module.
from dateutil import parser
from closest_station import find_closest_station_id

closest_stn_id = find_closest_station_id()
api_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/'
# url = api_url + str(closest_stn_id)
# Test Brompton Academy
url = api_url + str(505307)
# St Mary Magdalene Academy
url = api_url + str(1212453)

weather = get(url).json()

# example: how to get first record of weather
first_record = weather['items'][0]

temperatures = []

"""
Use a for loop to iterate over the temperatures and add to a list
for record in weather['data']:
    temperature = record['ambient_temp']
    temperatures.append(temperature)
"""

# better: list comprehension to get all the temperatures in a list
temperatures = [record['ambient_temp'] for record in weather['items']]

# list comprehension to get all the timestamps in a list
timestamps = [
    parser.parse(record['reading_timestamp'])for record in weather['items']
]

# create a plot of timestamps against temperature and show it
plt.plot(timestamps, temperatures)
## Set the axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
