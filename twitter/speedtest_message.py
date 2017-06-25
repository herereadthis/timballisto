"""Use SpeedTest CLI to send a tweet."""
# import os
import subprocess
from pprint import pprint
import json
# import time
# import datetime

tracking_file_path = './speedtest_tracking.json'


def bytes_to_string(bytes_string):
    """Convert Bytes object to a Python string."""
    return str(bytes_string, 'utf-8')


def json_string_to_dict(string):
    """Convert a string representation of JSON data to Python dictionary."""
    # json.loads is for loading from a string.
    return json.loads(string)


def bits_to_mbit(bit, decimal_places=2):
    """Convert bits to megabits (Mbit)."""
    mbit = bit / 2**20
    specification = '{0:.%sf}' % (decimal_places)
    return float(specification.format(mbit))


def append_and_write(existing_list, new_dict, file):
    """Create a new list with new entry and write to file."""
    existing_list.append(new_dict)
    json.dump(existing_list, file)


def record_speedtest(data):
    """Record the speedtest to a file."""
    try:
        with open(tracking_file_path, 'r+') as jsonfile:
            try:
                tracking_data = json.load(jsonfile)
                # this seek and truncate will wipe the previous JSON
                jsonfile.seek(0)
                jsonfile.truncate(0)
                append_and_write(tracking_data, data, jsonfile)

            except ValueError:
                print('data file has been corrupted')

    except FileNotFoundError:
        with open(tracking_file_path, 'w+') as jsonfile:
            tracking_data = []
            append_and_write(tracking_data, data, jsonfile)


def run_speedtest():
    """Run speed test and record the result."""
    try:
        print('Running speedtest....')
        speedtest_output = subprocess.check_output(['speedtest-cli', '--json'])
        print('Speedtest ran. ')

        speedtest_string = bytes_to_string(speedtest_output)
        speedtest_data = json_string_to_dict(speedtest_string)

        upload_speed = 'Upload Speed: %sMbits/s' % (
            bits_to_mbit(speedtest_data['upload'])
        )
        download_speed = 'Download Speed: %sMbits/s' % (
            bits_to_mbit(speedtest_data['download'])
        )

        print(upload_speed)
        print(download_speed)

        # list comprehension to pick the keys we need from the result
        keys = ['download', 'upload', 'timestamp']
        simple_data = {key: speedtest_data[key] for key in keys}

        record_speedtest(simple_data)

    except subprocess.CalledProcessError:
        print('Unable to run speedtest-cli...Wifi or Internet is down.')

    except Exception as inst:
        # To Do: handle all the various exceptions
        print(type(inst))
        print(inst.args)
        print(inst)


run_speedtest()
