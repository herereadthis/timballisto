"""Use SpeedTest CLI to send a tweet."""
import os
import pprint
import json
import time
import datetime

"""
def test():
    print('Running test')
    
   # with open('python /home/pi/speedtest/speedtest-cli --json') as json_data:
    #    data = json.load(json_data)
    #    print(data)
    
    a = os.popen('python3 /home/pi/speedtest/speedtest-cli --simple').read()
    print('ran')
    lines = a.split('\n')
    print(a)

"""



def test():

        #run speedtest-cli
        print('running test')
        a = os.popen("python /home/pi/speedtest/speedtest-cli --simple").read()
        print('ran')
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print(a)
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


test()
