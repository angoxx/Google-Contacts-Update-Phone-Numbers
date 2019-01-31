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