import pyperclip, re

text = pyperclip.pate()

patternObject = re.compile(''''

''', re.VERBOSE)
matchObject = patternObject.findall(text)
foundMatches = matchObject.group()

if foundMatches == False:
    pyperclip.copy("No matches found :(")
    print("No matches found :(")
else:
    pyperclip.copy(foundMatches)
    print(foundMatches)

#just insert the right pattern, then check if it works and what could go wrong
#then check answers agains automate-the-boting-stuff