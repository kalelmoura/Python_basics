import zipfile, os
from pathlib import Path

# os.mkdir("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook")
# open("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/file1.txt", 'w')
# open("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/file2.txt", 'w')
# open("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook/file3.txt", 'w')

files = 

with zipfile.ZipFile("/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook1.zip", 'w') as backup:
    backup.write('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/AlsPythonBook', compress_type=zipfile.ZIP_DEFLATED,
        compresslevel=9)





