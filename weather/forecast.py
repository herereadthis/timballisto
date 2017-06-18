"""Use OpenWeatherMap to do weather forecasting."""

from requests import get
from datetime import datetime, timedelta
from json import loads
from pprint import pprint
from auth import (
    open_weather_map_key
)