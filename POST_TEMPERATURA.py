import requests

payload = {
    "temperatura" : "5"
}

response = requests.post('http://192.168.83.103/temperatura', json=payload)
for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)