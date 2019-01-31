# Google contacts update phone

Update every phone number on Google Contacts using the Google people api.

# How to use

1. You'll need to create a credentials file in json. Follow this tutorial for set up the api and get the json file. https://cloud.google.com/video-intelligence/docs/common/auth
2. Put the json file in the same folder as the "main.py" and "util.py"
3. Launch the main.py
4. A new page in your web browser will open, you'll have to log in if you're not and accept the app to have access to your Google Contacts
5. You can close the page and the script will work and print "name: name-of-user : non-formatted-number -> formatted-number"

# Requirements

```
pip install phonenumbers
pip install google-api-python-client
pip install backoff
```

The script use Python 3

# About

This script use the phonenumbers library for formatting correctly all numbers with all country phone code. It use the Google people api for getting and updatting all numbers. When the script have finished, a CSV file will be created in the same folder as the script. If you have any contact with a phone number but without a name, the phone number will be added to the file. You'll be able to see if you have a phone number without a name and change it.