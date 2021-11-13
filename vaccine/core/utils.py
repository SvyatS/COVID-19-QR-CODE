def hidden_name(text):
    return text[0].upper() + "*" * (len(text) - 1)

def hidden_passport_serial(text):
    return text[:2] + "*" * (len(text) - 1)

def hidden_passport_number(text):
    return "*" * (len(text) - 3) + text[-3:]

def vaccine_structure(user):
    name = {
        "first_name": hidden_name(user.first_name),
        "middle_name": hidden_name(user.middle_name),
        "last_name": hidden_name(user.surname)
    }

    # valid_until =

    return name