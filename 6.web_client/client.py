import json
import urllib.request

url = 'http://127.0.0.1:5000/hello'
data = {
    'value': 123,
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)

with urllib.request.urlopen(req) as res:
    body = res.read()
    print(body.decode())

