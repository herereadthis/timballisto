"""Calculate the distance between two points, given latitude and longitude."""

# https://www.raspberrypi.org/learning/fetching-the-weather/worksheet2/

from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """Convert degrees to radians."""
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    # find the difference between two longitudes and latitudes
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    # calculate the distance between two points
    # **2 means to the power of two (squared)
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    # 6371 is the radius of the Earth
    distance = 2 * asin(sqrt(a)) * 6371
    return distance
