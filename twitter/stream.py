# tutorial here:
# https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/

# sudo pip3 install twython --upgrade
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# modify the default behavior of TwythonStreamer
# Since it is a class, extend it by creating a new class which inherits the
# functionality of TwythonStreamer, and modify any parts we may need to
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print('@%s: %s' % (username, tweet))

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


# run this, then in a separate python shell, run update_status.py
# you should see this show the stream update.
stream.statuses.filter(track='raspberryfoo')
