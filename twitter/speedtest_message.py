"""Use SpeedTest CLI to send a tweet."""

import subprocess
from pprint import pprint
import json
import errno
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

tracking_file_path = './speedtest_tracking.json'


class SpeedStatus:
    """Create SpeedTest class."""

    def __init__(self, key, secret, token, token_secret):
        """Initialize stuff."""
        self.tracking_file_path = tracking_file_path
        self.twitter = Twython(key, secret, token, token_secret)
        self.upload_mbits = None
        self.download_mbits = None
        self.speedtest_data_full = {}
        self.speedtest_data_simple = {}

    def set_tracking_file_path(self, filepath=tracking_file_path):
        """Set the filepath of the history file."""
        self.tracking_file_path = filepath

    def bytes_to_string(self, bytes_string):
        """Convert Bytes object to a Python string."""
        return str(bytes_string, 'utf-8')

    def json_string_to_dict(self, string):
        """Convert a string representation of JSON data to Python dict."""
        # json.loads is for loading from a string.
        return json.loads(string)

    def bits_to_mbit(self, bit, decimal_places=2):
        """Convert bits to megabits (Mbit)."""
        mbit = bit / 2**20
        specification = '{0:.%sf}' % (decimal_places)
        return float(specification.format(mbit))

    def append_and_write(self, existing_list, file):
        """Create a new list with new entry and write to file."""
        existing_list.append(self.speedtest_data_simple)
        json.dump(existing_list, file)

    def set_up_down_speeds(self):
        """Set the upload and download test numbers."""
        try:
            print('Running speedtest....')
            speedtest_output = subprocess.check_output(
                ['speedtest-cli', '--json']
            )
            print('Speedtest ran.\n\n')

            speedtest_string = self.bytes_to_string(speedtest_output)

            # the full data is not yet really needed, but keeping it anyway.
            full_data = self.json_string_to_dict(speedtest_string)

            # list comprehension to pick the keys we need from the result
            keys = ['download', 'upload', 'timestamp']
            simple_data = {key: full_data[key] for key in keys}

            self.speedtest_data_simple = simple_data
            self.speedtest_data_full = full_data
            self.upload_mbits = self.bits_to_mbit(simple_data['upload'])
            self.download_mbits = self.bits_to_mbit(simple_data['download'])

        except Exception as inst:
            # To Do: handle all the various exceptions
            print(type(inst))
            print(inst.args)
            print(inst)

    def print_up_down_speeds(self):
        """Get up and down speeds."""
        upload_speed = 'Upload Speed: %sMbps' % (self.upload_mbits)
        download_speed = 'Download Speed: %sMbps' % (self.download_mbits)

        print(upload_speed)
        print(download_speed)
        pprint(self.speedtest_data_simple)

    def record_speedtest(self):
        """Make a record of this speed test to compare with past tests."""
        try:
            with open(self.tracking_file_path, 'r+') as jsonfile:
                try:
                    tracking_data = json.load(jsonfile)
                    # this seek and truncate will wipe the previous JSON
                    jsonfile.seek(0)
                    jsonfile.truncate(0)
                    self.append_and_write(tracking_data, jsonfile)

                except ValueError:
                    print('data file has been corrupted')
        except OSError as e:
            if e.errno == errno.ENOENT:
                # The proper way to do FileNotFoundError, a subclass of OSError
                with open(tracking_file_path, 'w+') as jsonfile:
                    tracking_data = []
                    self.append_and_write(tracking_data, jsonfile)
            else:
                raise e

    def send_speed_tweet(self):
        """Send a tweet with speed test numbers."""
        if self.upload_mbits is not None and self.download_mbits is not None:
            message = 'Raspberry Pi Internet speed test'
            message = '%s: upload: %sMbps, download: %sMbps' % (
                message, self.upload_mbits, self.download_mbits
            )
            print(message)
            self.twitter.update_status(status=message)
        else:
            print('unable to get speed data')


# Check to see if this file is run as a module (import) or not
if __name__ == '__main__':
    # send_speed_tweet()
    status = SpeedStatus(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    status.set_up_down_speeds()
    status.record_speedtest()
    status.send_speed_tweet()
