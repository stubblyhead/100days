import requests

apikey = '82e02b0e5f8c8f22d9091f0c8d12dab2'
params = {'lat':39.0, 'lon':-101.0, 'cnt': 4, 'appid':apikey}


response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params)
response.raise_for_status()
print(response.status_code)
response = response.json()

might_rain = False
for r in response['list']:
    if r['weather'][0]['id'] < 700:
        might_rain = True

if might_rain:
    print('It will probably rain in the next 12 hours.')
else:
    print('It will probably not rain in the next 12 hours.')