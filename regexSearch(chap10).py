from pathlib import Path
import re

folder = input("What folder would you like to search? (absolute path required): ")
pattern = input("Enter a regular expression: ")
filePattern = re.compile(fr'{pattern}')

folderPath = Path(folder)
fileList = list(folderPath.glob('*.txt'))


for element in fileList:
    fileObj = open(element)
    fileContent = fileObj.readlines()
    for line in fileContent:
        fileSearch = filePattern.search(line)
        if not fileSearch:
            continue
        print(line, end="")
    fileObj.close()


