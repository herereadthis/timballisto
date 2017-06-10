import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from secret import twitter_keys

twitter_consumer_key = twitter_keys['consumer_key']
twitter_consumer_secret = twitter_keys['consumer_secret']
twitter_access_token = twitter_keys['access_token']
twitter_access_token_secret = twitter_keys['access_token_secret'] 
