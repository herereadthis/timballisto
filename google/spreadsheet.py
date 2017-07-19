"""Update a spreadsheet."""

import gspread
# import google.auth
# from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials

# from auth import (
#     drive_api
# )

# credentials = service_account.Credentials.from_service_account_info(
#     drive_api)

# credentials = service_account.Credentials.from_service_account_file(
#     'credentials.json')
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope
)

gc = gspread.authorize(credentials)
