import shutil
import os
from send2trash import send2trash
from pathlib import Path
h = Path.home()
print(h)
# (h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam' ).mkdir(exist_ok=True)
with open(h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')

# create folder, file and text inside file

shutil.copy(h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam/file1.txt', h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam/file2.txt')
# shutil.copytree(h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam', h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam_backup')
#(h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam2').mkdir()
# shutil.move(h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam/file1.txt', h / '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam2')
# shutil.rmtree('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam2')
# os.unlink('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter11/spam/file2.txt')
send2trash.send2trash('file1.txt')

