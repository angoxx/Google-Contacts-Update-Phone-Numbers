from __future__ import print_function


def format_phone(phone):

    if len(phone) == 13:
        char_number = list(phone)
        if char_number[0] == "+":
            char_number.insert(3, ' ')
            char_number.insert(8, ' ')
            correct_num = "".join(str(x) for x in char_number)
            return correct_num
        else:
            char_number.pop(0)
            char_number.pop(8)
            char_number.insert(0, "+")
            char_number.insert(1, "4")
            char_number.insert(2, "4")
            char_number.insert(3, " ")
            correct_num = "".join(str(x) for x in char_number)
            return correct_num

    if len(phone) == 14:
        char_number = list(phone)
        char_number.insert(3, ' ')
        correct_num = "".join(str(x) for x in char_number)
        return correct_num

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
                    return correct_num
                if char_number[3] != ' ':
                    char_number.insert(3, ' ')
                    if char_number[12] == ' ':
                        char_number.pop(12)
                    correct_num = "".join(str(x) for x in char_number)
                    return correct_num
            else:
                return phone

    if len(phone) == 16:
        char_number = list(phone)
        if char_number[2] == '4':
            if char_number[4] == '7':
                if char_number[1] == "+":
                    char_number.pop(1)
                    if char_number[3] != " ":
                        char_number.insert(3, " ")
                if char_number[12] == " ":
                    char_number.pop(12)
                    correct_num = "".join(str(x) for x in char_number)
                    return correct_num
        else:
            return phone

    if len(phone) == 17:
        char_number = list(phone)
        char_number.pop(12)
        char_number.pop(12)
        correct_num = "".join(str(x) for x in char_number)
        return correct_num

    if len(phone) > 17:
        char_number = list(phone)
        if char_number[2] == "4":
            char_number.pop(16)
            char_number.pop(16)
            char_number.pop(12)
            correct_num = "".join(str(x) for x in char_number)
            return correct_num
        else:
            return phone
