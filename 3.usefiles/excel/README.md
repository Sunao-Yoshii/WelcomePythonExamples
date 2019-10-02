# Excel の I/O

私がこれを使ってる理由は何か？
みんな Excel 好きすぎるからです…

Excel は良いプロダクトなのに変な使い方をやらせ過ぎです…そんなひどいシートを手で使いたくありませんでした。
だから Python で弄るのです。

## Excel 操作用ライブラリインストール

Python をインストールすると、漏れなく pip というコマンドがインストールされます。
これは node でいう所の npm みたいなもの、Ruby なら gem みたいなものです。

```sh
$ pip install openpyxl
```

`openpyxl` が目的のライブラリ。

## 早速操作してみよう

と言っても書いて、開き直して読むだけ。

```python
import openpyxl as px

# Excel を新規に作成
book = px.Workbook()
sheet = book.active

sheet['A1'] = 'Welcome to my broken show!'
book.save("sample.xlsx")

# Excel を開いて値の読み取り
book = px.load_workbook('sample.xlsx')

print(book.sheetnames)
sheet = book['Sheet']
print(sheet['A1'].value)
```

うん、シンプルで OK.