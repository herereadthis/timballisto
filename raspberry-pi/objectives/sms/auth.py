"""Grab Twilio Authentication Keys to authenticate."""

import json

with open('./../../../secret.json') as json_data:
    data = json.load(json_data)
    account_sid = data.get('twilio', {}).get('accountSID', {})
    auth_token = data.get('twilio', {}).get('authToken', {})
    sendee_phones = data.get('twilio', {}).get('sendeePhones', [])
    sender_phone = data.get('twilio', {}).get('senderPhone', {})
