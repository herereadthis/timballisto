"""Use SpeedTest CLI to send a tweet."""
import os
import subprocess
import pprint
import json
import time
import datetime


def convertBytesToString(bytes_string):
    """Converts Bytes object to a Python string."""
    return str(bytes_string, 'utf-8')


def convertJsonStringToDict(string):
    """Converts a string representation of JSON data to Python dictionary."""
    return json.loads(string)


def test():

        #run speedtest-cli
        print('running test')
        #a = os.popen("python /home/pi/speedtest/speedtest-cli --simple").read()
        speedtest_output = subprocess.check_output(['speedtest-cli', '--json'])
        print('ran')

        speedtest_string = convertBytesToString(speedtest_output)
        speedtest_data = convertJsonStringToDict(speedtest_string)

        pprint(speedtest_data)

        

        """
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print(date,p, d, u)
        """


test()
