import requests


response = requests.get('http://192.168.83.103/temperatura')

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)