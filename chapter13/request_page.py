import requests

response = requests.get(('https://automatetheboringstuff.com/files/rj.txt'))
# Response object
print(type(response))
# True if download succeeded | False if download failed
print(bool(response.status_code == requests.codes.ok))
# how many characters the URL has
print(len(response.text))
# from character 1 (index 0) to 210 (index 209)
print(response.text[:210])
