from pathlib import Path
import re

path = input("Absolute path to a .txt file: ")
fileObj = open(path)
text = fileObj.read()
fileObj.close()

regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
matchText = regex.findall(text)

finalText = text

for element in matchText:
    replacement = input(f"Enter a {element}: ")
    if element == 'ADJECTIVE':
        replacementRegex = re.compile('ADJECTIVE')
        finalText = replacementRegex.sub(replacement, finalText, count=1)
    if element == 'NOUN':
        replacementRegex = re.compile('NOUN')
        finalText = replacementRegex.sub(replacement, finalText, count=1)
    if element == 'ADVERB':
        replacementRegex = re.compile('ADVERB')
        finalText = replacementRegex.sub(replacement, finalText, count=1)
    if element == 'VERB':
        replacementRegex = re.compile('VERB')
        finalText = replacementRegex.sub(replacement, finalText, count=1)

print(finalText)

resultFile = open('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/MadLibs/MadLibs2.txt', 'w')
resultFile.write(finalText)
resultFile.close()
        



# no AI
# ask the user for an absolute path to a .txt file
# read that text file
# find patterns to the words: ADJECTIVE, NOUN, ADVERB or VERB
# prompt the user to replace the word classes that are found
# replace them
# print the results on the terminal
# create a new file with the results