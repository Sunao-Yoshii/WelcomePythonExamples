# Jupiter notebook

for Python 3.7.x

公式には https://jupyter.org/ を参照してください。  
これは一体どう言ったアプリかというと、

1. Webサーバ場で Python/R と言った言語を操作し、REPL 表示できる
2. Markdown などを選択的に挟むことで、動作説明文書としてそのまま活用できる

とか色々書きましたが、言い方を変えると「（文書内のコードが）実行可能なドキュメント環境」と言えると思います。

## Jupiter notebook インストール

Anaconda を利用してインストールした人は、この手順は必要ありません。  
Python3.x がインストールされている場合、以下のコマンドでインストールが可能です。

```bash
$ pip install --upgrade pip
$ pip install jupyter
```

## Jupiter notebook 起動

これ自体はコマンドを実行するだけです。  
このリポジトリを clone している場合は、`notebook/notebook_with_data/notebooks` にカレントを移動し、次のコマンドを実行します。

```sh
$ jupyter notebook
```

すぐにブラウザが起動し、次の様な画面が表示されているはずです。