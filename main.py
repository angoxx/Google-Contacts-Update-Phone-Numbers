from __future__ import print_function
import util


def main():
    """Update phone number in google contacts
    """

    # Connect to GContacts
    connections = util.credentials()

    for person in connections:

        # Get the name by person
        names = person.get('names', [])
        if names:
            name = names[0].get('displayName')

            # Get the phone number by person
            phones = person.get('phoneNumbers', [])
            if phones:
                phone = phones[0].get('value')

                # Show difference after formatting
                util.update_phone(phone, name)


if __name__ == '__main__':
    main()