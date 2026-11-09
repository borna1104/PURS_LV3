import requests

payload = {
    "username" : "PURS",
    "password" : "1234"
}

response = requests.post('http://192.168.83.103/login', data=payload)

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)