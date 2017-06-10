import random
# sudo pip3 install twython --upgrade
from twython import Twython
from auth import (
    twitter_consumer_key as consumer_key,
    twitter_consumer_secret as consumer_secret,
    twitter_access_token as access_token,
    twitter_access_token_secret as access_token_secret
    )

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

messages = [
    'Hello world!',
    'Hi there',
    'What\'s up?',
    'How\'s it going?',
    'Have you been here before?',
    'Get a hair cut!'
    ]
message = random.choice(messages)

# how to upload just a status
# twitter.update_status(status=message)

#how to upload status with image
with open('./resources/images/babbage_1024x1024.jpg', 'rb') as photo:
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids = [response['media_id']])

print('Tweeted: %s' % message)
