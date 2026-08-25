
import zipfile, os, re
from pathlib import Path

# os.mkdir("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook")
# open("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/file1.txt", 'w')
# open("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/file2.txt", 'w')
# open("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/file3.txt", 'w')


# def backup_to_zip():

#     i = 1

#     pattern = re.compile(r'/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook\d*\.zip')

#     folder = Path("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff")

#     for item in folder.iterdir():
#         if pattern.search(str(item)):
#             i = i+1
            
#     files = os.listdir("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook")
    
#     with zipfile.ZipFile(f"/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook{i}.zip", 'w') as zipFile:
#         for item in files:
#             zipFile.write(f'/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/{item}', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


# backup_to_zip()


def backup_to_zip():
    i = 1

    pattern = re.compile(r'.*\d*\.zip')

    zips = os.listdir('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff')

    for item in zips:
        if pattern.search(item):
            i = i+1

    files = os.listdir('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook')
    with zipfile.ZipFile(f'/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook{i}.zip', 'w') as zipFile:
        for item in files:
            zipFile.write(f'/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/{item}', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

backup_to_zip()
























