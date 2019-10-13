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
