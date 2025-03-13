import requests

parms = { 'lat': 45.0, 'lng': -123.0, 'formatted': 0 }

response = requests.get('https://api.sunrise-sunset.org/json',params=parms)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']


response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
long = data['iss_position']['longitude']
lat = data['iss_position']['latitude']

print(lat, long)
