"""Use SpeedTest CLI to send a tweet."""
import os
import subprocess
from pprint import pprint
import json
import time
import datetime
import speedtest as st

servers = []

s = st.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.share()

results_dict = s.results.dict()


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


def record_speedtest(data):
    try:
        file = open(tracking_file_path, 'r')
        print('tracking file exists')
        # json.load is for loading a file.
        tracking_list = json.load(file)
    except FileNotFoundError:
        file = open(tracking_file_path, 'w')
        print('creating tracking file')
        tracking_list = []
        
    print(tracking_list)


def test():
    try:
        print('Running speedtest....')
        speedtest_output = subprocess.check_output(['speedtest-cli', '--json'])
        print('Speedtest ran. ')

        speedtest_string = bytes_to_string(speedtest_output)
        speedtest_data = json_string_to_dict(speedtest_string)

        pprint(speedtest_data)
        print('\n\n')

        upload_speed = 'Upload Speed: %sMbits/s' % (
            bits_to_mbit(speedtest_data['upload'])
        )
        download_speed = 'Download Speed: %sMbits/s' % (
            bits_to_mbit(speedtest_data['download'])
        )

        print(upload_speed)
        print(download_speed)

        keys = ['download', 'upload', 'timestamp']

        simple_data = {key: speedtest_data[key] for key in keys}

        record_speedtest(simple_data)

        pprint(simple_data)
        
    except subprocess.CalledProcessError:
        print('Unable to run speedtest-cli...Wifi or Internet is down.')
        
    except Exception as inst:
        # To Do: handle all the various exceptions
        print(type(inst))
        print(inst.args)
        print(inst)
        

    


test()
