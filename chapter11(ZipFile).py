import zipfile
('/Users/gabrielkalel/programing/ZipFiles').mkdir(exist_ok=True)
with open('/Users/gabrielkalel/programing/ZipFiles/file1.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello' * 10000)

with zipfile.ZipFile('/Users/gabrielkalel/programing/ZipFiles/example.zip', 'w') as example_zip:
    example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

print(example_zip.namelist())
file1_info = example_zip.getinfo('file1.txt')
print(file1_info.file_size)
print(file1_info.compress_size)
example_zip.close()
example_zip.extractall('/Users/gabrielkalel/programing/ZipFiles')
example_zip.close()


