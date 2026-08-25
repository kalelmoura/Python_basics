import re

# string password detection

# rules:
#  must be at least 8 characters long
#  contain uppercase and lowercase characters
#  have at least 1 digit

passwordTest = "Gabi2525"

def validatePassword(text):
    if ' ' in text:
        print("No space in the password is allowed")
        return

    regex1 = re.compile(r'.{8,}')
    regex2 = re.compile(r'[a-z]+')
    regex3 = re.compile(r'[A-Z]+')
    regex4 = re.compile(r'\d+')
    match1 = regex1.search(text)
    match2 = regex2.search(text)
    match3 = regex3.search(text)
    match4 = regex4.search(text)

    if match1 is None or match2 is None or match3 is None or match4 is None:
        print("This password is invalid, try again.")
    else:
        print("Password saved.")

validatePassword(passwordTest)






