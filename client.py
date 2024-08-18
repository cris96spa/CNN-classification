import json
import requests

params = {'image_path' : 'app/images'}

url = 'http://localhost:8000/predict/'

#data = json.dumps(data)
response = requests.post(url, params=params)

print(response.url)
print(response.status_code)
print(response.json())
