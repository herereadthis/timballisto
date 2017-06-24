"""Use SpeedTest CLI to send a tweet."""
import os
import subprocess
from pprint import pprint
import json
import time
import datetime


def convertBytesToString(bytes_string):
    """Converts Bytes object to a Python string."""
    return str(bytes_string, 'utf-8')


def convertJsonStringToDict(string):
    """Converts a string representation of JSON data to Python dictionary."""
    return json.loads(string)


def convertBitsToMbit(bit, decimal_places = 2):
    """Converts bits to megabits (Mbit)."""
    mbit = bit / 2**20
    specification = '{0:.%sf}' % (decimal_places)
    return float(specification.format(mbit))


def test():
        print('running test')
        speedtest_output = subprocess.check_output(['speedtest-cli', '--json'])
        print('ran')

        speedtest_string = convertBytesToString(speedtest_output)
        speedtest_data = convertJsonStringToDict(speedtest_string)

        pprint(speedtest_data)
        print('\n\n')

        upload_speed = 'Upload Speed: %sMbits/s' % (
            convertBitsToMbit(speedtest_data['upload'])
        )
        download_speed = 'Download Speed: %sMbits/s' % (
            convertBitsToMbit(speedtest_data['download'])
        )

        print(upload_speed)
        print(download_speed)

    


test()
