# CSV の I/O

CSV を弄っていきます...がその前に

## まずはファイルの IO だ

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
readFile = open('pitFile_UTF-8.txt', mode='r', encoding='utf-8', newline='\n')
# readline/readlines で読み込めるが、行単位で取り出せるものの改行コードは除去しない
readLines = [x.strip() for x in readFile.readlines()]
print(readLines)
```

## CSV も読み書きしよう

CSV 読み取りにはパーサーが存在します。
csv は標準のライブラリですので、特に追加のインストールを必要とはしません。

```python
import csv

# シンプルに配列を書き込む
with open('outFile.csv', mode='w', encoding='utf-8') as wf:
    outdata = [
        ['Id', 'Name', 'Cost'],
        ['01', '白き鋼鉄のX', '3818'],
        ['02', 'Ori and the Blind Forest Definitive Edition', '1900']
    ]
    writer = csv.writer(wf)
    writer.writerows(outdata)

# 読み取り
with open('outFile.csv', mode='r', encoding='utf-8') as rf:
    readlines = csv.reader(rf)
    # イテレートオブジェクトなので、List に変換して出力
    print(list(readlines))
```

結果は

```
[['Id', 'Name', 'Cost'], ['01', '白き鋼鉄のX', '3818'], ['02', 'Ori and the Blind Forest Definitive Edition', '1900']]
```

これでは扱い辛いでしょうか？
辞書型での操作もあります。

```python
# 辞書として書き込む
with open('outFileDict.csv', mode='w', encoding='utf-8') as wf:
    varline = {'Id': '01', 'Name': '白き鋼鉄のX', 'Cost':3818 }
    writer = csv.DictWriter(wf, ['Id', 'Name', 'Cost'])
    writer.writeheader()
    writer.writerow(varline)

# 読み込み手段
with open('outFileDict.csv', mode='r', encoding='utf-8') as rf:
    readlines = csv.DictReader(rf)
    print(list(readlines))
```
