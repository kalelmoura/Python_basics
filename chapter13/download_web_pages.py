import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# raises an exeption with status code (404, 401, 200..) if the download failed
response.raise_for_status()
# create a file, 'wb' is write mode in bytes, because we will be writig in the file with bytes, because each 'chunk' is bytes
with open('/Users/gabrielkalel/Projects/Python/Automate_Boring_stuff/chapter13/RomeoAndJuliet.txt', 'wb') as play_file:
    # reads the file in chunks, it's a safer practice than downloading it all at once
    for chunk in response.iter_content(100000):
        play_file.write(chunk)

