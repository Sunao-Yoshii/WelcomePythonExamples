# チュートリアル

for Python 3.7.x

といっても、非エンジニア向けではないので、非常にざっくり記述します。

## 世界に挨拶するところ

おなじみですね。  
文字列は `"` か `'` で囲み、`print` 関数で出力します。

    REPL は コンソール上で `python` とだけ入力すると起動します。
    終了する場合は `exit()` を呼び出すことで終了します。


REPL で実行してます。

```python
>>> print('Hello World')
Hello World
>>> message = "Python"
>>> print(f'Hello {message}')
Hello Python
>>>
```

見たままですね。

    Python はオブジェクト指向も対応していますが、Java/C# のような強制はしません。
    使いたければ使えば良いというスタンスです。

`f'Hello {message}'` は fstring と呼ばれる埋め込み構文ですね。  
もちろんフォーマットなどもしたいでしょうから、format も使ってみます。

でも使い方忘れました（素です^^;）  
使い方から見ましょうか

```python
>>> help('')
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 ...(中略)
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 ```

 文字列型のメソッドで `format` ありましたね。

```python
>>> 'ひゃっはー {0} だぜー'.format(message)
'ひゃっはー Python だぜー'
```

## 変数と四則演算

文字列を変数に入れるのはできましたので、他のものもさっくり

```python
>>> num_var = 1000
>>> num_var
1000
>>> num_var = 3.1415
>>> num_var
3.1415
>>> bool_val = True
>>> bool_val
True
>>> str_var = 'HEHEHE'
>>> str_var
'HEHEHE'
>>> str_var[0]
'H'
```

基本ですし軽く流しますね。  
あとは char/byte 型が存在します…といえば、コンパイル系言語いじってる人にはわかってもらえるかと。

## リストと辞書

リストというとわかりやすいと思いますが、あのリストです。  
Python ですと他言語で言う所の配列的にも利用してます。

```python
>>> value = [1, 2, 4, 8, 16, 32]
>>> for v in value:
...     print(v)
...
1
2
4
8
16
32
```

辞書については他言語を触っていれば「ハッシュマップ」と言えば理解できると思います。

```python
>>> value = { 'Id':1, 'Name':'Ori and the blind forest' }
>>> for k in value:
...     print(f'key: {k}, value: {value[k]}')
...
key: Id, value: 1
key: Name, value: Ori and the blind forest
```

### リストの展開

関数型言語の方の方がお馴染みだとは思いますが

```python
>>> value = [1, 'hoge']
>>> head, tail = value
>>> head
1
>>> tail
'hoge'
```

ちなみに、List のサイズと合わないとこんなメッセージが出ます。

```python
>>> value = [1, 2, 4, 8, 16, 32]
>>> head, tail = value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

### リストのアクセス

リストには様々な取得方法があります。  
インデックスを使ったアクセス

```python
>>> value = [1, 2, 4, 8, 16, 32]
>>> value[2]
4
>>> value[-1]
32
```

スライス(取り出した新しいリストを作成して返します)

```python
>>> value[2:]
[4, 8, 16, 32]
>>> value[:3]
[1, 2, 4]
>>> value[2:4]
[4, 8]
```

インデックスを指定しないことで、リストのコピー(Shallow copy)を作成。

```python
>>> value[:]
[1, 2, 4, 8, 16, 32]
```

## 制御文

といってもみたままでしょう。  
python の場合、for はイテレータを利用するので、インクリメントループはあまり見ません。

```python
>>> for i in range(0, 10):
...     if i > 5:
...         break
...     else:
...         print(i)
...
0
1
2
3
4
5
```

### 後置 if と三項演算子の代わり

みなさん三項演算子好きですか？私は大好きです。  
というか普通の言語で if ブロック作るとか冗長すぎてキレそうになります。

```java
int amount;
if (id > 0) { amount = 10 } else { amount = 500; }
// これでええやん。final にできるし最高じゃない？
final int amount = id > 0 ? 10 : 500;
```

Python はこれを後置 if で処理します。

```Python
>>> id = 10
>>>
>>> amount = 10 if id > 0 else 500
>>> print(amount)
10
```

書式的には `(条件がTrueのときの値) if (条件) else (Falseのときの値)` ですね。

## 関数構文

安心してください。見たままです。  
１言語でも弄っていれば、見ればわかるはずです。

```python
>>> def append_str(name:str) -> str:
...     return f'Hello {name}'
...
>>> append_str('function')
'Hello function'
```

Python はブロックをインデントで表します。  
インデントの深さが異なれば違うブロックと解釈されるので、インデントによる見やすさが言語仕様で強制されています。  
どうも嫌いな人には嫌いらしいのですが、インデントの高さはどうせ `{...}` ブロック言語でも合わせるものでしょうし、`{...}` にこだわる人の気持ちが良くわかりません…  
(ちなみに、Scala 3 として開発してる2019.09時点の Dotty に、オダスキー先生がインデントブロック入れようとしてめっちゃ反発されてます。なんか現実とか利点とか抜きに信仰感漂ってて草)

## オブジェクト指向

単純なオブジェクトは見たままでしょう。

```python
>>> class Example:
...     def __init__(self):
...         # コンストラクタ
...         self.message = 'object'
...     def fires(self):
...         # メソッド
...         return f'Hello {self.message}'
...
>>> ex_var = Example()
>>> ex_var.fires()
'Hello object'
```

もちろん継承できます

```python
>>> class ExampleExtends(Example):
...     def __init__(self):
...         super(ExampleExtends, self).__init__()
...         self.message = self.message + ' appendMessage'
...
>>> ex_var = ExampleExtends()
>>> ex_var.fires()
'Hello object appendMessage'
```

多重継承です

```python
>>> class AnotherOne:
...     def hello(self):
...         return 'Hello!'
...
>>> class Doubles(Example, AnotherOne):
...     pass
...
>>> ex_var = Doubles()
>>> ex_var.hello()
'Hello!'
>>> ex_var.fires()
'Hello object'
>>>
```

## そしてファイルに書き出そう

拡張子 py を使用してダイルアウトプットすることができます。

```python
# 昔はファイルのエンコーディングを先頭に書きましたが、Python3 は UTF-8 が原則なので、不要になりました。
# output.py の中身
class Simplly:
    def __init__(self, name: str):
        self.__name = name

    def name(self):
        return self.__name
```

読み込んで使いましょう

```python
# main.py
# import で呼び出します。
# なお、検索パスは実行ディレクトリをルートとした相対パスです

from outfile import Simplly

simpl = Simplly('ヒャッハー')
print(simpl.name())
```

入力だって受け付けられます。  
`input_example.py` として用意しています。

```python
import sys

# 引数の読み取り
print(sys.argv)

# 入力を求めることもできます
input_val = input('input value > ')
print(input_val)
```

実行してみると

```bash
$ python input_example.py 
['input_example.py']
input value > aaa
aaa
```

## 推奨はしないけど技法

### リスト内包表記 & 後置 if

リストを変換して別リストを作成する場合の選択と、変換をまとめて行います。  
偶数の項目のみ 2 乗して取得します。

```python
>>> nums = range(10)
>>> changes = [x ** 2 for x in nums if x % 2 == 0]
>>> changes
[0, 4, 16, 36, 64]
```

### ラムダ式(関数オブジェクト)

関数を引数に持つ場合に、関数をその場で作成して使用することもできます。  
ただし注意したいのは Pytnon は純粋関数型言語ではないので、スタックには必然的に限界はありますし、全てを遅延する（Haskell）のようなことはできません。

```python
>>> function_var = lambda x: x ** 2
>>> function_var(2)
4
```

当然関数も代入可能です

```python
>>> def twice(x: int) -> int:
...     return x ** 2
...
>>> function_var = twice
>>> function_var(2)
4
```
