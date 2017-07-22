"""Send an SMS file with Twilio."""

from twilio.rest import Client
from auth import (
    account_sid,
    auth_token,
    owner_phone,
    sender_phone
)

client = Client(account_sid, auth_token)

# to_number = '+%s' % owner_phone
to_number = '+17023250770'
from_number = '+%s' % sender_phone
message = 'Hello this is test message from Jimmy'

client.messages.create(to=to_number, from_=from_number, body=message)
