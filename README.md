sample project showing how to connect to Google Spreadsheets with a free account on PythonAnywhere


SETUP INSTRUCTIONS
==================
- setup new Google APIs Console project:
    - For that project, enable Google Drive API
    - create credentials for a new "user" (a service account with a project editor role). Save the json secrets file generated as secrets.json.
- create a new Google Spreadsheet called `Automated Spreadsheet` and share it with the `client_email` inside of json secrets (ie. the new bot "user" you just created with editor privileges)
- `pip install -r requirements.txt`


- reference https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
