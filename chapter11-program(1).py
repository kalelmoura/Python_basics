from pathlib import Path
h = Path.home()
(h / 'spam').mkdir(exist_ok=True)
(h / 'spam/eggs').mkdir(exist_ok=True)
(h / 'spam/eggs2').mkdir(exist_ok=True)
(h / 'spam/eggs/bacon').mkdir(exist_ok=True)
for f in ['spam/file1.txt', 'spam/eggs/file2.txt', 'spam/eggs/file3.txt',
'spam/eggs/bacon/file4.txt']:
    with open(h / f, 'w', encoding='utf-8') as file:
        file.write('Hello')

# created folders from home path, then a file creation loop

import os, shutil
from pathlib import Path
h = Path.home()

for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)
        # Rename file to uppercase:
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())
   
    print('')

# displays the folder name, subfolders and file names of the spam folder

