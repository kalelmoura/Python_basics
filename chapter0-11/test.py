import re


def is_strong_password(password):
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')

    if len(password) < 8:
        return False

    if uppercase_regex.search(password) is None:
        return False

    if lowercase_regex.search(password) is None:
        return False

    if digit_regex.search(password) is None:
        return False

    return True