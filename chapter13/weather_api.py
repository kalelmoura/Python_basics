import requests

# get lattitude and longitude
city_name='San Francisco'
state_code='CA'
country_code='US'
API_key='626e585a51d05a0cd67e8d6170af4e37'
# the URL is the endpoint
response=requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
response.text  # This is a Python string.
# '[{"name":"San Francisco","local_names":{"id":"San Francisco","lat":37.7790262,"lon":-122.419906,"country":"US","state":"California"}]'
# -> in JSON - python reads them in dictionaries
import json
response_data=json.loads(response.text)
response_data  # This is a Python data structure.
# [{"name":"San Francisco","local_names":{"id":"San Francisco","lat":37.7790262,"lon":-122.419906,"country":"US","state":"California"}]

lat=json.loads(response.text)[0]['lat']
lon=json.loads(response.text)[0]['lon']
print(f'lat={lat}|lon={lon}')

# get weather
response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
response_data=json.loads(response.text)
response_data
# {'coord': {'lon': -122.4199, 'lat': 37.779}, 'weather': [{'id': 803, 'timezone': -25200, 'id': 5391959, 'name': 'San Francisco', 'cod': 200}
temperature_kelvin=response_data['main']['temp']
# 285.44
temperature_celcius=round(temperature_kelvin-273.15,1)  # Convert Kelvin to Celsius.
# 12.3
temperature_fahrenheit=round(temperature_kelvin*(9/5)-459.67,1)  # Convert Kelvin to Fahrenheit.
# 54.1

# here we first requested, through the API, the lat and lon of San Francisco, then with that data made another request, through the API, for the weather

weather = response_data['weather'][0]['main']
print(weather)



