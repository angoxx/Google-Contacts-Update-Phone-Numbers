from __future__ import print_function


def format_plusfourfour(char_number):
    if char_number[3] != '1' or char_number[4] != '1':
        # delete every non int
        count = 0
        for x in char_number:
            count += 1
            if x == ' ' or x == '.' or x == '-':
                char_number.pop(count - 1)

        # Check if it's a mobile number
        if char_number[3] == '7':

            # check if phone number have the correct len - 13 - +440000000000
            if len(char_number) == 13:
                char_number.insert(3, ' ')
                char_number.insert(8, ' ')

        # return the formatted number
        correct_num = "".join(str(x) for x in char_number)
        return correct_num


def format_phone(phone):
    """Reformat every uk mobile number to the correct format like: +44 0123 456789"""

    char_number = list(phone)

    # for all ++44 - delete one +
    if char_number[1] == "+":
        char_number.pop(1)

        correct_num = format_plusfourfour(char_number)

        return correct_num

    # for all 07 - delete 0 and add +44
    elif char_number[0] == "0" and char_number[1] == '7':
        char_number.pop(0)
        # 7000 000000 or 7000 000 000
        char_number.insert(0, "+")
        char_number.insert(1, "4")
        char_number.insert(2, "4")

        # return the formatted number
        correct_num = format_plusfourfour(char_number)
        return correct_num

    # for all +44
    elif char_number[0] == '+' and char_number[1] == '4' and char_number[2] == '4':

        if char_number[3] == '7' or char_number[3] == ' ' and char_number[4] == '7':
            correct_num = format_plusfourfour(char_number)
            return correct_num

    # For no + before 44
    elif char_number[0] == '4' and char_number[1] == '4' and char_number[2] == '7':
        char_number.insert(0, '+')

        correct_num = format_plusfourfour(char_number)

        # return the formatted number
        return correct_num
