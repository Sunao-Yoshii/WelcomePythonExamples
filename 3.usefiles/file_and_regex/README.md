# ファイルの操作と正規表現(ログ解析など)

for Python 3.7.x

## まずはファイルの IO

プレーンテキストの I/O なら初めから関数が存在しています。  
安直に `open` 関数を使用します。

開発者なら見た方が早いですね。

```python
# デフォルトは UTF-8 なので、明示は必要ないのですが一応
outFile = open('pitFile_UTF-8.txt', mode='w', encoding='utf-8', newline='\n')

# 描き込み描き込み
contents = [
    'Line1 いちぎょうめ\n',
    '一体何が悪いのか！？政治が悪いのか！？\n'
]

# write は１要素のみ描き込み
# writelines はシーケンスを書き込むが、改行コードはいれてくれない
outFile.writelines(contents)
outFile.flush()
outFile.close()

# 読み込み
# なお、改行コードは明示しなければ OS の標準として認識されるようです
readFile = open('pitFile_UTF-8.txt', mode='r', encoding='utf-8', newline='\n')
# readline/readlines で読み込めるが、行単位で取り出せるものの改行コードは除去しない
readLines = [x.strip() for x in readFile.readlines()]
print(readLines)
```

## ファイル/ディレクトリ操作

ファイルを操作するなら、ディレクトリも操作しないと嘘でしょう。  
サンプルコードを列挙します。

### 存在チェック


```python
>>> import os
>>> os.path.exists('./README.md')
True
```

### それはファイル？

```python
>>> import os
>>> os.path.isfile('./README.md')
True
```

### それはディレクトリ？

```python
>>> import os
>>> os.path.isdir('README.md')
False
```

### ディレクトリ作成

```python
>>> import os
>>> os.mkdir('./new_dir')
>>> os.path.isdir('./new_dir')
True
```

### 削除

```python
>>> import os
>>> os.remove("./NEW_README.md")
```

ディレクトリの削除(ただし空のみ)

```python
>>> import os
>>> os.rmdir("./dummyDir")
```

ディレクトリをファイルごと

```python
>>> import shutil
>>> shutil.rmtree("./copy2")
```

### コピー

```python
>>> import shutil
>>> shutil.copy('./README.md', './NEW_README.md')
'./NEW_README.md'
```

フォルダごとコピー

```python
>>> import shutil
>>> shutil.copytree("./tutorial", "./copy2")
'./copy2'
```

### 移動

```python
>>> import shutil
>>> shutil.move("./tutorial/README.md", "./another.md")
'./another.md'
```

## ファイル情報参照系

### ファイル名と拡張子を分離

```python
>>> import os
>>> ftitle, fext = os.path.splitext('./tutorial/README.md')
>>> ftitle
'./tutorial/README'
>>> fext
'.md'
```

### パスからのファイル名取得

```python
>>> import os
>>> os.path.basename('./tutorial/README.md')
'README.md'
```

### ディレクトリとファイル名分離

```python
>>> import os
>>> os.path.split('/path/to/test1.txt')
('/path/to', 'test1.txt')
```

### ファイル検索

再帰検索する場合は「recursive」を指定する必要がある位です。

```python
>>> import glob
>>> glob.glob('./*/*.md')
['tutorial/README.md', 'install/README.md']
>>> glob.glob('./**/*.md', recursive=True)
['./README.md', './tutorial/README.md', './install/README.md', './usefiles/excel/README.md', './usefiles/file_and_regex/README.md', './usefiles/csv/README.md']
```

## 正規表現

ここまで来ると、システム監査とかでログ情報をごにょごにょするのに役立つはずです。  
ですがそれだけではちょっと足りない。

あるあるパターンで、ログをマッチングして抽出するケースなんかがあるでしょう。  
例えば下記は Tomcat のアクセスログ例です。

`127.0.0.1 - - [16/Jan/2012:23:08:31 +0900] "GET /hoge/huga.do HTTP/1.1" 200 4682 "http://localhost:8090/hoge/huga.do" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"`

前述ですでにファイルの検索/IO は話しているので、このログをマッチさせ、値を抽出することを考えてみます。  
ざっくり形状を考えれば

`(IP) - - [(アクセス時刻)] "(HTTP動詞) (URL) (プロトコル)" (ステータス) (データサイズ) "フルURL" "クライアント情報"`

正規表現だとこんな感じでしょうか？

`((\d{,3}\.){3}\d{1,3}) - - \[([A-Za-z\d/: +]+)\] "([A-Z]+) ([^ ]*) ([^"]*)" (\d+) (\d+) "([^ ]+)" "(.*?)"`

### ライブラリのインポート

標準ライブラリなので、追加インストールは不要です。

```python
>>> import re
```

### 正規表現にまずはマッチさせる

`re.match(exp, log)` を利用して正規表現評価を行います。  
なお、一致しない場合このメソッドは None （他言語なら null とか nil とかそんな感じのもの）を応答します。

```python
>>> log = '127.0.0.1 - - [16/Jan/2012:23:08:31 +0900] "GET /hoge/huga.do HTTP/1.1" 200 4682 "http://localhost:8090/hoge/huga.do" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"'
>>> exp = r'((\d{,3}\.){3}\d{1,3}) - - \[([A-Za-z\d/: +]+)\] "([A-Z]+) ([^ ]*) ([^"]*)" (\d+) (\d+) "([^ ]+)" "(.*?)"'
>>> result = re.match(exp, log)
>>> result
<re.Match object; span=(0, 170), match='127.0.0.1 - - [16/Jan/2012:23:08:31 +0900] "GET />
```

    尚、r'' で囲った文字列はバックスラッシュのエスケープが不要となります。

### グループ化してる値を取得

JavaScript 同様に `if` 文は `None` などを検知したとき `False` と皆してくれますので、分岐条件にいれてしまいます。

```python
>>> if result:
...     result.groups()
... 
('127.0.0.1', '0.', '16/Jan/2012:23:08:31 +0900', 'GET', '/hoge/huga.do', 'HTTP/1.1', '200', '4682', 'http://localhost:8090/hoge/huga.do', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
```

### 正規表現のコンパイル

正規表現を実行するとき、処理系として以下の行動を行います。

1. 正規表現を、一致処理ようの内部モデルに変換
2. 内部モデルに一致するかどうかの判定

うち 1 の処理は結構重たい処理なので、事前にコンパイルしておくことができます。

```python
>>> compiled = re.compile(r'((\d{,3}\.){3}\d{1,3}) - - \[([A-Za-z\d/: +]+)\] "([A-Z]+) ([^ ]*) ([^"]*)" (\d+) (\d+) "([^ ]+)" "(.*?)"')
>>> result = compiled.match(log)
>>> result.groups()
('127.0.0.1', '0.', '16/Jan/2012:23:08:31 +0900', 'GET', '/hoge/huga.do', 'HTTP/1.1', '200', '4682', 'http://localhost:8090/hoge/huga.do', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
```

### 補足：日付時刻の扱い

日付文字列を取得したら、「二つの日付文字列から経過秒数を計算したい」のような要望があるはず（性能問題が出た時の対処）。  
ということで、日付型の扱いです

#### datetime インポート

とりあえず使ってみます。

```python
>>> import datetime
>>> 
>>> datetime.date.today()
datetime.date(2019, 9, 29)
>>> datetime.datetime.now()
datetime.datetime(2019, 9, 29, 12, 31, 35, 288047)
 ```

#### 日付のパース

使用できる書式は [公式](https://docs.python.org/ja/3/library/datetime.html#strftime-strptime-behavior) に記載があります。

```python
>>> datetime.datetime.strptime('16/Jan/2012:23:08:31 +0900', '%d/%b/%Y:%H:%M:%S %z')
datetime.datetime(2012, 1, 16, 23, 8, 31, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
```

#### 時間差と日付の計算

時間差を出すのは非常に簡単で、ようするに引き算すればよいです。

```python
>>> start = datetime.datetime.strptime('16/Jan/2012:23:08:31 +0900', '%d/%b/%Y:%H:%M:%S %z')
>>> end = datetime.datetime.strptime('16/Jan/2012:23:11:21 +0900', '%d/%b/%Y:%H:%M:%S %z')
>>> 
>>> end - start
datetime.timedelta(seconds=170)
```

では、3 日後を計算してみます。

```python
>>> delta = datetime.timedelta(days=5)
>>> delta + start
datetime.datetime(2012, 1, 21, 23, 8, 31, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
```

   尚、ここでは触れていませんが、datime はミリ秒まで対応しています。  
   書式などは 公式 https://docs.python.org/ja/3/library/datetime.html#strftime-strptime-behavior を参照してください。

## ログと統計に使えそうな基本組み込み関数

`len`: リストなど列挙系オブジェクトの要素数を取得する。

```python
>>> len([1, 2, 3, 8, 16])
5
```

`max`: 列挙要素から最大値を取得。

```python
>>> max([1,2,4,8,16])
16
```

`min`: 最小値の取得

```python
>>> min([1,2,4,8,16])
1
```

`sum`: リストなど列挙系の値の合計

```python
>>> sum([1, 2, 4, 8])
15
```

`zip`: 二つのリストを組み合わせてタプルのリストを作成する

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
```

`filter`： 第一引数でフィルタ条件、第二引数に Iterable を流し込むと、条件に一致する列挙型が作成されます。  
この例ではそのままだと表示できないので、`list()` で List 型へ変換しています。

```python
>>> filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
<filter object at 0x108a8b150>
>>> list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
[2, 4, 6]
```

各種統計機能。  
数値の入ったリストであればまとめて処理できます。

```python
from statistics import mean, median,variance,stdev

data = [100,200,300,400,500,500,600,700,800,800]

m = mean(data)
median = median(data)
variance = variance(data)
stdev = stdev(data)
print('平均: {0:.2f}'.format(m))
print('中央値: {0:.2f}'.format(median))
print('分散: {0:.2f}'.format(variance))
print('標準偏差: {0:.2f}'.format(stdev))
```