import os, re, shutil
from pathlib import Path

# creates a string of the formatted version of the progression of the numbers of the files -> 001, 002, 003 
def formattedNumbers(number):
    if number < 10:
        number = f'00{str(number)}'
    elif number < 100:
        number = f'0{str(number)}'
    else:
        number = str(number)
    # returns the formatted number to be atributed to the 'i' variable later on
    return number


spamPath = '/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam'

# creates files 1-120 inside the 'spam' folder, skipping files: 42, 86, 103
def createFiles():
    for i in range(1, 121):
        if i not in (42, 86, 103):
            with open(f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam{str(i).zfill(3)}.txt', 'w') as file:
                pass

# creates list of files from the 'spam' folder that start with 'spam'
def listSpamFiles():

    # creates a list of all files inside the 'spam' folder
    files = os.listdir('/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams')
    fileList = []

    # loops 120 times (the highest numbered file inside 'spam')
    # the lentgh of the 'files' list is 117, however we need this to loop to 120, hence the +4 after the len(files) (keep in mind the last value of the range() function gets excluded, so to reach 120 it needs to be 121)
    for i in range(1, len(files)+4):
        # makes 'i' into the formatted version of the numbers of the files -> 001, 002, 003
        i = formattedNumbers(i)
        # loops every loop
        # searches through every file ('len(files)') to find a match to the desired numbered file progression
        # if a match is found, appends the relative path of that file (or the name) into a list (fileList)
        for y in range(len(files)):
            # pattern of the desired numbered progression
            pattern = re.compile(fr'spam{i}\..*')
            # searches through the files one by one, one loop at a time, to find a match
            if pattern.search(files[y]):
                fileList.append(files[y])
    # function returns the filesList so a global variable of that list can be created
    return fileList

fileList = listSpamFiles()

# finds gaps in the fileList and fills them by renaming all the files after the gap to the right number progression
def renumberFiles():

    lengthList = len(fileList)
    # since i is being replaced by a string of the formatted number progression, we still need a variable to loop from 0 to len(fileList)
    x = 0   

    # loops through all the file names of the list to find any gaps
    for i in range(1, lengthList+1):
        # makes 'i' into the formatted version of the numbers of the files -> 001, 002, 003
        i = formattedNumbers(i)
        # gathers the current given file name
        file = fileList[x]
        # gathers the number of the given file name
        fileNumber = str(file[4]+file[5]+file[6])
        # catches any gap in the file name number progression
        if i != fileNumber:
            # gathers the pattern of the suffix of the given file name
            patternSuffix = re.compile(fr'\..*')
            # searches through the file name to find the suffix, places the match/matches into a list
            matchedSuffix = patternSuffix.findall(file)
            # gets the first (and in this case: only) match
            suffix = matchedSuffix[0]
            # until the file that fills the gap found by the if statement doesn't exist, rename the current file (the one that exists after the gap of the numbered files) to the number that the progression is suppost to be at
            while Path(f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam{i}{suffix}').is_file() == False:
                # renaming the file
                shutil.move(f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/{file}', f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam{i}{suffix}')
        x = x+1

renumberFiles()

    
