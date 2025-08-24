"""Find the closest weather station."""

# https://www.raspberrypi.org/learning/fetching-the-weather/worksheet2/

# Python HTTP requests
from requests import get
# import json
# “pretty-print” arbitrary Python data structures
from pprint import pprint
# from the created haversine file in this directory
from haversine import haversine

base_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/'
stations = base_url + 'getallstations'
weather = base_url + 'getlatestmeasurements/'

# latitude and longitude of intersection of Washington St and Broad St
my_lat = 38.882252
my_lon = -77.171082

all_stations = get(stations).json()['items']


def find_closest():
    # the longest distance between any two points on earth is 20036km
    # basically we want to find a station that is less than that
    smallest = 20036
    for station in all_stations:
        # this will just print out all the stations
        # print(station)
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        # run the stations through the haversine formula
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        # if this distance is the smallest so far in the for loop, then save it
        # into the closes_station variable
        if distance < smallest:
            smallest = distance
            closest_station = station
    return closest_station


def find_closest_station_id():
    closest_station = find_closest()
    return closest_station['weather_stn_id']


def print_closest():
    closest_station = find_closest()
    weather_url = weather
    weather_url = weather_url + str(closest_station['weather_stn_id'])

    print('Closest weather station is {0} (ID: {1})' .format(
        closest_station['weather_stn_name'],
        closest_station['weather_stn_id']))
    print('Lat: {0}, Long: {1}' .format(
        closest_station['weather_stn_lat'],
        closest_station['weather_stn_long']))
    closest_weather = get(weather_url).json()['items']
    pprint(closest_weather)


if __name__ == '__main__':
    print_closest()
