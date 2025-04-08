import requests

with open('totallynotpasswords.txt') as f:
    APP_ID, API_KEY = f.readline().split()

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': ''
    ''
}

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
query = input('what did you do?  ')
data = {'query': query, 'weight_kg': 90, 'height_cm': 183, 'age': 45}

response = requests.post(url=endpoint, headers=headers, data=data)

response.raise_for_status()
print(response.json()['exercises'])