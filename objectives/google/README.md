# Google Integration

Connect a Raspberry Pi to Google services.

## Installation

```bash
# Super simple Google Spreadsheets Python API
pip install gspread


# Python library for accessing resources protected by OAuth 2.0
# oauth2client is deprecated and the official recommendation is use google-auth
# but google-auth is incompatible with gspread
sudo pip install oauth2client
```

## Get Google OAuth2 Credentials

* Go to the [Google Developers Console](https://console.developers.google.com/project) and make a new project.
[//]: # * Then go to [Google Cloud Console Dashboad](https://console.cloud.google.com), select your new project, and click to "Enable API." Choose "Drive API" because we want to mess with Google Spreadsheets.
* Find the link to "Credentials" to create a new "Service Account Key."
* Then find the link to "Enable" and click on that
* Create a new service account, probably "Project > Owner" and give it an account name. Choose "JSON" key type and create.
* Save these credentials; **do not save in version control!**
* Create and name a new spreadsheet. Make a note of its ID, which you can find in the URL.
* Find the button to share. Add the email that is included in the credentials JSON.