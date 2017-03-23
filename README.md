# fieldbook-com-google-spreadsheet

That mini app is about Data Transfer between fieldbook.com to Google Drive -> spreadsheets

Codes are written and tested with Python 3.5

Python library requirements are;
pip3 install --upgrade google-api-python-client
pip3 install fieldbook_py

First, in first, you have to sign in to fieldbook.com
Then create a table and then a sheet.
Top of the right you can see API button.
If you click this button, you can see API access information.
You have to change line 50 with that information.

You must read Google API document which URL is https://developers.google.com/sheets/api/quickstart/python

You have to change spreadsheet ID value and "client_scret.json" file.
