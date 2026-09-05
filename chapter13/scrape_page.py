import requests, bs4
from pathlib import Path

# download weather page
response = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7889712&lon=-122.3954798')
response.raise_for_status()

path = Path('/Users/gabrielkalel/Projects/Python_basics/Automate_Boring_stuff/chapter13/weather.html')

# if the html file isnt already in my hardrive, download it
if path.is_file() == False:
    with open('/Users/gabrielkalel/Projects/Python_basics/Automate_Boring_stuff/chapter13/weather.html', 'wb') as file:  
        for chunks in response.iter_content(100000):
            file.write(chunks)
        
with open('/Users/gabrielkalel/Projects/Python_basics/Automate_Boring_stuff/chapter13/weather.html') as file:  
    soup = bs4.BeautifulSoup(file, 'html.parser')
    tags = soup.select('#current_conditions-summary')
    print(str(tags))

# --------------------------------------------------- with no hard drive download ---------------------------------------------------------------------
# response = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7889712&lon=-122.3954798')

# soup = bs4.BeautifulSoup(response.text, 'html.parser')
# tags = soup.select('#current_conditions-summary')
# print(str(tags))

