import os, re, shutil
from pathlib import Path

def createFiles():
    for i in range(1, 121):
        if i not in (42, 86, 103):
            with open(f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam{str(i).zfill(3)}.txt', 'w') as file:
                pass

createFiles()

# def listSpamFiles():

#     files = os.listdir('/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams')
#     fileList = []
#     for i in range(len(files)+2):
#         i = i+1
#         if i < 10:
#             i = f'00{str(i)}'
#         elif i < 100:
#             i = f'0{str(i)}'
#         else:
#             i = str(i)
#         for y in range(len(files)):
#             pattern = re.compile(fr'spam{i}\..*')
#             if pattern.search(files[y]):
#                 fileList.append(files[y])
#     return fileList

# fileList = listSpamFiles()

# def renumberFiles():

#     lengthList = len(fileList)
#     x = 0   

#     for i in range(lengthList):
#         i = i+1
#         if i < 10:
#             i = f'00{str(i)}'
#         elif i < 100:
#             i = f'0{str(i)}'
#         else:
#             i = str(i)
#         spam = f'spam{i}'
#         file = fileList[x]
#         fileSpam = str(file[0]+file[1]+file[2]+file[3]+file[4]+file[5]+file[6])
#         if spam != fileSpam:
#             # print(spam)
#             # print(fileSpam)
#             patternSuffix = re.compile(fr'\..*')
#             matchedSuffix = patternSuffix.findall(file)
#             suffix = matchedSuffix[0]
#             while Path(f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam{i}{suffix}').is_file() == False:
#                 shutil.move(f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/{file}', f'/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter0-11/spams/spam{i}{suffix}')
#         x = x+1

# renumberFiles()

    
