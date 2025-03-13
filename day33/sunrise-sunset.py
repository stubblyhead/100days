import requests

response = requests.get('https://api.sunrise-sunset.org/json?lat=45.0&lng=-123.0')
response.raise_for_status()

data = response.json()
sunrise = data['sunrise']
sunset = data['sunset']
