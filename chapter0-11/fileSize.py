import os, re, shutil
from pathlib import Path

files = os.listdir('/Users/gabrielkalel/Downloads/Documentos')


for item in files:
    item = f'/Users/gabrielkalel/Downloads/Documentos/{item}'
    sizeMB = os.path.getsize(item) / 1000000
    if sizeMB >= 1:
        print(item)

        

