import requests

API = 'http://api.open-notify.org/iss-now.json'
r = requests.get(API)
r.raise_for_status()

data = r.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_position = (latitude,longitude,)

print(iss_position)