from pathlib import Path
import os
file_path = Path('programing', 'Python', 'Automate_Boring_Stuff')
print(file_path)

print(file_path.is_absolute())

absolute_file_path = file_path.absolute()

print(absolute_file_path.is_absolute())

print(Path.home())

print(Path.cwd())

os.chdir('/Users/gabrielkalel/programing/Python/Add_Time')
print(Path.cwd())


os.chdir('/Users/gabrielkalel/programing/Python/Automate_Boring_stuff')
print(Path.cwd())



