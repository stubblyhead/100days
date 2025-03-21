import requests
import os
import datetime

date = datetime.date.today().strftime('%Y%m%d')
endpoint = 'https://pixe.la/v1/users/stubblyhead/graphs/vitamins'
payload = {
    'date':date,
    'quantity':'1'
}

token = os.environ.get('TOKEN')
headers = {
    'X-USER-TOKEN': token
}

response = requests.post(url=endpoint, json=payload, headers=headers)
response.raise_for_status()

print(response.text)