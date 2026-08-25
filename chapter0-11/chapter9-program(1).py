#find emails and phone numbers inside copied text (clipboard)

import pyperclip, re

text = pyperclip.paste()

patternObj = re.compile(r'\+\d{2}\s\d{4}\s\d{6} | [^\s@]+@[^\s@]+\.[^\s@]+') # phone number | email address
matchObj = patternObj.findall(text) # .findall gives the answer in a string

if not matchObj: # if the string is empty: []
    pyperclip.copy(f"No matches found :(")
else:
    matches = "\n".join(matchObj) # joins the string into a text and separates elements by new-lines
    pyperclip.copy(matches)
