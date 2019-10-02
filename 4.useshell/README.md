# シェルとの共存

for Python 3.7.x

シェルとの相互運用周りを行うサンプルです。

## Python スクリプト

Python を　`python` コマンド引数でなく実行する方法です。  
先頭に `#!/usr/bin/python` を突っ込んで実行権限を与えます。

```python
#!/usr/bin/python
print('fire')
```

この状態で実行権限を付与して実行します。

```sh
$ chmod +x hello.py
$ ./hello.py
fire
```

## パイプから呼び出す処理を作成する

パイプから呼び出される際、その値は標準入力から設定されます。  
注意点として、ある程度まとまった結果を標準入力でまとめて受け流という点です。

サンプルとして `simple.py` を用意しました。

```python
#!/usr/bin/python
import os
import sys

value = sys.stdin.read()  # パイプの入力
value = value.replace('//', '/')  # / が // として入力されるのでリプレース

splitted = value.split("\n")  # 改行で分解し
for line in splitted:
    if os.path.isfile(line):  # それがファイルで
        filename, ext = os.path.splitext(line)
        if '.txt' == ext:  # 拡張子が txt なら中身を表示します
            with open(line, mode='r') as rf:
                print(''.join(rf.readlines()))
```

そして実行してみる。  
1行目はファイル構成。この値が標準入力に入ってきます。

```sh
$ find ./sampleTexts/
./sampleTexts/
./sampleTexts//dontcall.md
./sampleTexts//example.txt
$ 
$ chmod +x simple.py
$ find ./sampleTexts/ | ./simple.py 
Hello python: shell command.
```

## Python からシェルコマンドを実行する

一番わかりやすいところで `ls` コマンドをサブプロセスとして呼んでみます。  
`shell_command.py` というファイル名で作成してます。

```python
#!/usr/local/bin/python3
import subprocess
proc = subprocess.run(["ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc.stdout.decode("utf8"))
```

## 単純にパイプを呼び出す

パイプを実行するもっともシンプルな方法。  
`simple_pipe.py` として保存。

```python
#!/usr/local/bin/python3
import subprocess

res = subprocess.check_output(
    "ls | grep si",
    shell=True,
    stderr=subprocess.STDOUT)

print(res.decode())
```

## Python からパイプを実行してみる

といってもパイプのアウトプットを連結するだけです。  
途中に Python 処理を挟みたければ挟めば？って用途ですね。

`pipe_basic.py` として用意します。

```python
#!/usr/local/bin/python3
import subprocess

p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "py"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()

result = p2.communicate()[0]
print(result.decode())
```
