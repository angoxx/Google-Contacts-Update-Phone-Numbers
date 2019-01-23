from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def update_phone(phone, name):

            if len(phone) == 13:
                char_number = list(phone)
                if char_number[0] == "+":
                    char_number.insert(3, ' ')
                    char_number.insert(8, ' ')
                    correct_num = "".join(str(x) for x in char_number)
                    print(name + " : " + phone + " -> " + correct_num)
                else:
                    char_number.pop(0)
                    char_number.pop(8)
                    char_number.insert(0, "+")
                    char_number.insert(1, "4")
                    char_number.insert(2, "4")
                    char_number.insert(3, " ")
                    correct_num = "".join(str(x) for x in char_number)
                    print(name + " : " + phone + " -> " + correct_num)

            if len(phone) == 14:
                char_number = list(phone)
                char_number.insert(3, ' ')
                correct_num = "".join(str(x) for x in char_number)
                print(name + " : " + phone + " -> " + correct_num)

            if len(phone) == 15:
                char_number = list(phone)
                if char_number[2] == '4':
                    if char_number[8] != ' ':
                        if char_number[1] == "+":
                            char_number.pop(1)
                            char_number.insert(3, ' ')
                            char_number.insert(8, ' ')
                            if char_number[4] == "0":
                                char_number.pop(4)
                                char_number.pop(7)
                                char_number.insert(8, ' ')
                            correct_num = "".join(str(x) for x in char_number)
                            print(name + " : " + phone + " -> " + correct_num)
                        if char_number[3] != ' ':
                            char_number.insert(3, ' ')
                            if char_number[12] == ' ':
                                char_number.pop(12)
                            correct_num = "".join(str(x) for x in char_number)
                            print(name + " : " + phone + " -> " + correct_num)
                    else:
                        print(name + " : " + phone)

            if len(phone) == 16:
                char_number = list(phone)
                if char_number[2] == '4':
                    if char_number[4] == '7':
                        if char_number[1] == "+":
                            char_number.pop(1)
                            if char_number[3] != " ":
                                char_number.insert(3," ")
                        if char_number[12] == " ":
                            char_number.pop(12)
                            correct_num = "".join(str(x) for x in char_number)
                            print(name + " : " + phone + " -> " + correct_num)
                else:
                    print(name + " : " + phone)

            if len(phone) == 17:
                char_number = list(phone)
                char_number.pop(12)
                char_number.pop(12)
                correct_num = "".join(str(x) for x in char_number)
                print(name + " : " + phone + " -> " + correct_num)

            if len(phone) > 17:
                char_number = list(phone)
                if char_number[2] =="4":
                    char_number.pop(16)
                    char_number.pop(16)
                    char_number.pop(12)
                    correct_num = "".join(str(x) for x in char_number)
                    print(name + " : " + phone + " -> " + correct_num)
                else:
                    print(phone)


def credentials():
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
        personFields='names,emailAddresses,phoneNumbers').execute()
    connections = results.get('connections', [])

    return connections