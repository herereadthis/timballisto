"""Grab Google Drive API Keys to authenticate."""

import json

with open('./../../../secret.json') as json_data:
    data = json.load(json_data)
    drive_api = data.get('google', {}).get('driveAPI', {})
