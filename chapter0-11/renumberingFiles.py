import os, re, shutil
from pathlib import Path


SPAM_PATH = Path('/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams')


# Creates a string of the formatted version of the progression
# of the numbers of the files -> 001, 002, 003
def format_number(number):
    if number < 10:
        number = f'00{str(number)}'
    elif number < 100:
        number = f'0{str(number)}'
    else:
        number = str(number)

    # Returns the formatted number to be attributed to the number variable later on
    return number


# Creates files 1-120 inside the 'spam' folder,
# skipping files: 42, 86, 103
def create_files():
    for file_number in range(1, 121):
        if file_number not in (42, 86, 103):
            with open(SPAM_PATH / f'{str(file_number).zfill(3)}.txt', 'w') as spam_file:
                pass


# Creates a list of files from the 'spam' folder that start with 'spam'
def list_spam_files():

    # Creates a list of all files inside the 'spam' folder
    files = os.listdir(SPAM_PATH)

    file_list = []

    # Loops 120 times (the highest numbered file inside 'spam')
    # The length of the 'files' list is 117; however, we need this
    # to loop to 120, hence the +4 after len(files)
    # Keep in mind the last value of range() is excluded,
    # so to reach 120 it needs to be 121
    for file_number in range(1,len(files)+4):

        # Makes file_number into the formatted version
        # of the numbers of the files -> 001, 002, 003
        file_number = format_number(file_number)

        # Searches through every file to find a match
        # to the desired numbered file progression.
        for file_index in range(len(files)):

            # Pattern of the desired numbered progression
            pattern = re.compile(fr'spam{file_number}\..*')

            # Searches through the files one by one to find a match
            if pattern.search(files[file_index]):
                file_list.append(files[file_index])

    return file_list


file_list = list_spam_files()


# Finds gaps in file_list and fills them by renaming all the files
# after the gap to the correct number progression
def renumber_files():

    list_length = len(file_list)

    # Since expected_number is replaced by a formatted string,
    # file_index is used to progress through file_list.
    file_index = 0

    # Loops through all file names in the list to find gaps
    for expected_number in range(1, list_length + 1):

        # Makes expected_number into the formatted version
        # of the numbers of the files -> 001, 002, 003
        expected_number = format_number(expected_number)

        # Gets the current file name
        file_name = file_list[file_index]

        # Gets the number of the given file name
        file_number = str(file_name[4] + file_name[5] + file_name[6])

        # Catches any gap in the file number progression
        if expected_number != file_number:

            # Gets the pattern of the suffix of the given file name
            suffix_pattern = re.compile(r'\..*')

            # Searches through the file name to find the suffix
            matched_suffixes = suffix_pattern.findall(file_name)

            # Gets the first and, in this case, only match
            suffix = matched_suffixes[0]

            # Until the file that fills the gap does not exist,
            # rename the current file to the expected number.
            while Path(SPAM_PATH / f'spam{expected_number}{suffix}').is_file() == False:
                shutil.move(SPAM_PATH /f'{file_name}', SPAM_PATH / f'spam{expected_number}{suffix}')

        file_index = file_index + 1


renumber_files()