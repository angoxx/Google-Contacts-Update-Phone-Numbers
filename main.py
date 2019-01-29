from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import util

# Contacts Scope for the api
SCOPES = ['https://www.googleapis.com/auth/contacts']


def main():
    """Update phone number in google contacts
    """

    # Connect to GContacts
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1900,
        personFields='names,emailAddresses,phoneNumbers').execute()
    connections = results.get('connections', [])

    for person in connections:

        # Get etag and resourceName by person - needed for proceed to the update
        etag = person.get('etag')
        resourcename = person.get('resourceName')

        # Get the name by person
        names = person.get('names', [])
        if names:
            name = names[0].get('displayName')

        # Get the phone number by person
        phones = person.get('phoneNumbers', [])
        if phones:
            phone = phones[0].get('value')

            # Call list of formatted numbers
            formatted_number = util.format_phone(phone)

            if formatted_number:
                print(name + " : " + phone + " -> " + formatted_number)

                # Update contacts numbers
                service.people().updateContact(
                    resourceName=resourcename,
                    body={
                        'resourceName': 'people/*',
                        'etag': etag,
                        "phoneNumbers": [{"value": formatted_number}]
                    },
                    updatePersonFields="phoneNumbers",
                ).execute()


if __name__ == '__main__':
    main()
