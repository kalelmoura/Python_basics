# def is_phone_number(text):
#     if len(text) != 12:  # Phone numbers have exactly 12 characters.
#         return False
#     for i in range(0, 3):  # The first three characters must be numbers.
#        if not text[i].isdecimal():
#             return False
#     if text[3] != '-':  # The fourth character must be a dash.
#         return False
#     for i in range(4, 7): # The next three characters must be numbers.
#        if not text[i].isdecimal():
#             return False
#     if text[7] != '-':  # The eighth character must be a dash.
#         return False
#     for i in range(8, 12):  # The next four characters must be numbers.
#        if not text[i].isdecimal():
#             return False
#     return True

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     segment = message[i:i+12]
#     if is_phone_number(segment):
#         print('Phone number found: ' + segment)
# print('Done')

# manual way to text pattern match

# now with regular expressions:

import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}') # get pattern object
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.') # get a match object
match_obj.group() # get the string of matched text


