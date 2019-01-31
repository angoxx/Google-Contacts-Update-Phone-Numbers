from __future__ import print_function
import util


def main():
    """
    - Update mobile number in google contacts to correct format -
    """

    # Connect to GContacts by Google People API
    connections, service = util.connection()

    # Blank name list
    blank_lst = []

    # Get every GContacts users one by one
    for person in connections:

        # Get etag and resourceName by person - needed for proceed to the update
        etag = person.get('etag')
        resource_name = person.get('resourceName')

        # Get the name by person
        names = person.get('names', [])
        name = ""
        if names:
            name = names[0].get('displayName')

        # Get the phone number by person
        phones = person.get('phoneNumbers', [])
        if phones:
            phone_value = phones[0].get('value')

            # Format the number and return it
            formatted_number = util.format_numbers(phone_value)

            # if there is a formatted number, update it in GContacts
            if formatted_number != "":

                # Show the difference
                print(name + " : " + str(phone_value) + " -> " + str(formatted_number))

                # Update the phone number in Google Contacts
                util.update_formatted_number(service, resource_name, etag, formatted_number)

                # Add the number in a list if the name is blank
                if name == "":
                    blank_lst.append(formatted_number)

    # Add the list of blank name in a CSV file
    util.blank_name_to_csv(blank_lst)


if __name__ == '__main__':
    main()
