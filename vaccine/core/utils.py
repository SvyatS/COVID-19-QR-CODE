from datetime import date, datetime, timedelta
from random import randint


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
    valid_until = (date.today() + timedelta(days=randint(20, 53))).strftime('%d.%m.%Y')
    date_birthday = user.date_birthday.strftime('%d.%m.%Y')

    content = {
        "full_name": name,
        "date_birthday": date_birthday,
        "valid_until": valid_until,
        "vaccine_id": '{} {} {} {}'.format(user.vaccine_id[:4], user.vaccine_id[4: 8], user.vaccine_id[8:12], user.vaccine_id[12:]),
        "passport": {
            "serial": hidden_passport_serial(user.passport_series),
            "number": hidden_passport_number(user.passport_number)
        }
    }

    return content
