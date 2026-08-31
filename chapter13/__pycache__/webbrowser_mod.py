import webbrowser
import pyperclip


if bool(pyperclip.paste()) == True:
    webbrowser.open(pyperclip.paste())
else:
    webbrowser.open('https://gabrielmoura.space') 