from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import backoff
import traceback
import csv
import phonenumbers


def connection():
    """ Connection to the google people api """

    credentials = None

    # Contacts Scope for the api
    scopes = ['https://www.googleapis.com/auth/contacts']

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            credentials = flow.run_local_server()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    service = build('people', 'v1', credentials=credentials)

    # Call the People API
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1900,
        personFields='names,emailAddresses,phoneNumbers').execute()
    connections = results.get('connections', [])

    return connections, service


def handle_backoff(details):
    """ Show the error during a backoff """

    print("Backing off {wait:0.1f} seconds afters {tries} tries "
          "calling function {target} with args {args} and kwargs "
          "{kwargs}".format(**details))
    traceback.print_exc()


@backoff.on_exception(backoff.expo, HttpError, max_tries=5, on_backoff=handle_backoff)
def update_formatted_number(service, resource_name, etag, formatted_number):
    """ Update on Google Contacts the phone number """

    # Update contacts numbers
    service.people().updateContact(
        resourceName=resource_name,
        body={
            'resourceName': 'people/*',
            'etag': etag,
            "phoneNumbers": [{"value": formatted_number}]
        },
        updatePersonFields="phoneNumbers",
    ).execute()


def blank_name_to_csv(blank_lst):
    """ Add a list of blank name to a CSV file """

    # Add the list of blank name to a csv file
    with open('blank_name.csv', 'wb') as csv_file:
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        wr.writerow(blank_lst)


def format_numbers(phone):
    """ Format the phone number with the phonenumbers library """

    # Parse the number in the library and return the phone code and the national number
    unformatted = phonenumbers.parse(phone, "GB")

    # Format the parsed number to the international format
    formatted = phonenumbers.format_number(unformatted, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    # Return the formatted number
    return formatted
