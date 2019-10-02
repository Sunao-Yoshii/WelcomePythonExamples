# Webクライアント

for Python 3.7.x

別の章で作成した REST サーバにリクエストを送ってみます。  
これを利用すればテストで REST API をコールし、その後のログを検証すると言ったことができる様になります。

 ## 標準 urllib.request を利用する

ここでは前章で説明した flask サーバに POST データを送信して結果を取得します。  
レスポンスからは Cookie なども取得できますので、それを利用すればログイン操作もおそらくできます。

```python
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
```

第二引数を省略すると GET リクエストになります。  
また、 `PUT, PATCH, DELETE` を指定する場合 `method='PUT'` の様な引数を追加することで実行できます。  
もちろん引数なしの `POST` も実行可能です。

実行してみた図です。

```bash
$ python client.py 
{
  "array_value": [
    1, 
    2, 
    4, 
    8, 
    16
  ], 
  "message": "Hello", 
  "status": 100
}

```

flask サーバ上では

```sh
127.0.0.1 - - [01/Oct/2019 20:56:48] "POST /hello HTTP/1.1" 200 -
```

という様な感じです。


## requests サードパーティライブラリを使う

さらに REST に特化し、簡単に利用できるライブラリとして、requests を紹介します。

```sh
$ pip install requests
```

Anaconda なら既に入っているかもしれません。  
これはさらに直感的にリクエストを送信するためのライブラリです。

`requests_client.py` というファイルにサンプルを用意しました。

```python
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
```

これでテストがやりやすくなるはず。
