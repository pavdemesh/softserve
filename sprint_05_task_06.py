import re


def valid_email(mail):
    pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

    try:
        if re.fullmatch(pattern, mail):
            print("Email is valid")
        else:
            raise ValueError

    except ValueError:
        print("Email is not valid")
        return


valid_email("trafioc@ukr_tel.com")
valid_email("trafic@ukr.tel.com")
valid_email("trafic@ukr.c0m")
