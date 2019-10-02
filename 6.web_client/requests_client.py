import requests

url = 'http://127.0.0.1:5000/hello'
data = {
    'value': 123,
}
headers = {
    'Content-Type': 'application/json',
}

resp = requests.post(url, json=data, headers=headers)

print(resp.status_code)
print(resp.cookies.get_dict())
print(resp.headers)
print(resp.json())
resp.close()
