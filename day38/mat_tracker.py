import requests
import datetime
import json

with open('totallynotpasswords.txt') as f:
    APP_ID, API_KEY = f.readline().strip().split()
    SHEETY_KEY = f.readline().strip()

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = f'https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts'
query = input('what did you do?  ')
ntx_data = {'query': query, 'weight_kg': 90, 'height_cm': 183, 'age': 45}

response = requests.post(url=nutritionix_endpoint, headers=headers, data=ntx_data)

response.raise_for_status()
exercises = []
for e in response.json()['exercises']:
    exercises.append([e['name'],e['duration_min'],e['nf_calories']])

now = datetime.datetime.today()
date = now.strftime('%m/%d/%Y')
time = now.strftime('%H:%M')

headers = {'Content-Type': 'application/json'}
for e in exercises:
    name,duration,cals = e
    hr = duration // 60
    min = duration % 60
    duration = f'{hr}:{min}'
    shy_data = {'workout': {'date': date, 'time': time, 'exercise': name, 'duration': duration, 'calories': cals}}
    shy_data = json.dumps(shy_data)
    requests.post(url=sheety_endpoint, data=shy_data, headers=headers)