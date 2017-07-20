"""Update a spreadsheet with gspread."""

import gspread
from datetime import datetime
# Official recommendation - currently incompatible with gspread.
# from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
from auth import (
    drive_api
)
spreadsheet_id = '1qWSmRq0ttzX7h4h6pymw6ryzaiVIn27DgiiXaBz7bzM'


class Spreadsheet:
    """Create a spreadsheet instance."""

    def __init__(self, credentials):
        """Initialize stuff."""
        self.scope = scope = ['https://spreadsheets.google.com/feeds']
        """
        The official gspread documention recommends using:
        ServiceAccountCredentials.from_json_keyfile_name() but that requires
        saving the JSON file somewhere, which can easily be put into version
        control by accident. Instead, save the JSON file somewhere else, then
        use a separate auth.py file to load the data as a dictionary.
        """
        self.credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            credentials, scope
        )
        self.gc = gspread.authorize(self.credentials)

    def set_worksheet(self, spreadsheet_id, worksheet_index=0):
        """Pick a spreadsheet to update.

        Remember to:
        * Actually create the spreadsheet
        * Share the spreadsheet with the email provided in credentials JSON
        """
        self.worksheet = self.gc.open_by_key(spreadsheet_id).get_worksheet(
            worksheet_index
        )

    def get_value(self, cell):
        """Get the value of a cell."""
        return self.worksheet.acell(cell).value


spreadsheet = Spreadsheet(drive_api)
spreadsheet.set_worksheet(spreadsheet_id)
timestamp = datetime.utcnow()
local_now = datetime.now()
# print(datetime.utcnow())
current_date = local_now.strftime('%Y-%m-%d')
current_time = local_now.strftime('%H:%M:%S')
print(local_now.strftime('%Y-%m-%d'))
print(local_now.strftime('%H:%M:%S'))
spreadsheet.worksheet.append_row([current_date, current_time])
