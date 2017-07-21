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
        self.cell_pos = {}

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

    def set_cell_position(self, row):
        """Set coordinates of row to work with."""
        self.cell_pos = {
            'start_date': 'A%s' % (row),
            'start_time': 'B%s' % (row),
            'end_date': 'C%s' % (row),
            'end_time': 'D%s' % (row),
            'duration': 'E%s' % (row)
        }

    def get_duration_formula(self):
        """Make duration."""
        c = self.cell_pos
        return '=(%s - %s) + (%s - %s)' % (
            c['end_date'], c['start_date'], c['end_time'], c['start_time']
        )


timestamp = datetime.utcnow()
local_now = datetime.now()

current_date = local_now.strftime('%Y-%m-%d')
current_time = local_now.strftime('%H:%M:%S')
print('Time and date: %s %s' % (current_date, current_time))

# Begin the spreadsheet instance.
spreadsheet = Spreadsheet(drive_api)
spreadsheet.set_worksheet(spreadsheet_id)
row_count = spreadsheet.worksheet.row_count

spreadsheet.set_cell_position(row_count)
c = spreadsheet.cell_pos
end_date_cell_value = spreadsheet.get_value(c['end_date'])

# If no end timer entry is found, add to last row
if end_date_cell_value == '':
    print('End Timer')
    duration = spreadsheet.get_duration_formula()
    spreadsheet.worksheet.update_acell(c['end_date'], current_date)
    spreadsheet.worksheet.update_acell(c['end_time'], current_time)
    spreadsheet.worksheet.update_acell(c['duration'], duration)
# Else, create new row with start timer entry
else:
    print('Start Timer')
    spreadsheet.worksheet.append_row([current_date, current_time])
