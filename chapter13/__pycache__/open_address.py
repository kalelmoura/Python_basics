# open_adress - get an address either from an argument from the command line or in the clipoard, and load a website with the address given

import webbrowser, sys, pyperclip

# sys.argv is a list, the first argument/element is the file_name, the second is the argument passed, if an argument is passed
# if there is a second argument (a street address ideally):
if len(sys.argv) > 1: 
    # we don't want the file_name, only the address, so [1:] is to remove the file_name
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

