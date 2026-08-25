import os, shutil, re

files = os.listdir('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter0-11')

pattern = re.compile(r'.*\.cfg')

for item in files:
    if pattern.search(item):
        shutil.move(f'/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter0-11/{item}', '/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter0-11/destination')


