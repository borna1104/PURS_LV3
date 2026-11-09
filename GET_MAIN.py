import requests

response = requests.get('http://192.168.83.103:80/')

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)