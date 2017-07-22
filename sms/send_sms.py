"""Send an SMS file with Twilio."""

from twilio.rest import Client
from auth import (
    account_sid,
    auth_token,
    owner_phone
)

client = Client(account_sid, auth_token)