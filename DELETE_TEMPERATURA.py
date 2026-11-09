import requests

response = requests.delete('http://192.168.83.103/temperatura?id=1')

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)