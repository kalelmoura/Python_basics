import pyperclip, re

text = pyperclip.paste()

patternObject = re.compile(r'''
\+\d{2}\s\d{4}\s\d{6} 
| 
[^\s@]+@[^\s@]+\.[^\s@]+
''', re.VERBOSE)
foundMatches = patternObject.findall(text)


if not foundMatches:
    pyperclip.copy("No matches found :(")
    print("No matches found :(")
else:
    result = "\n".join(foundMatches)

    pyperclip.copy(result)
    print(result)