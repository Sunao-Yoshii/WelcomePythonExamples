# WelcomePythonExamples

Python3.7+ から始める非 Python 利用者向けの、「Pythonでこんなことできるよ」の説明用リポジトリです。  
あまり深い内容には言及せず、紹介程度にサンプルを記述するリポジトリです。

「こんなのもPythonらしいしやってほしい、紹介してほしい」などがあればプルリクでも Issues でもお願いします。  
Issues にどれくらい書き込まれるかは不明ですが、できる範囲かつ、やる気のある物を対応していく方針です。  
無償かつ趣味でやってますのでその辺りはご容赦を。

## はじめに Python の利点

### スクリプト言語で速攻開始できる

Python はスクリプト言語なので、テキストソースをそのまま実行できます。  
これは書いてすぐ試せるという利点に繋がります。  
なぜ UT を書くのでしょう？ リグレッションテストという観点はありますが、もう一つの観点はコンパイル言語では

1. モジュールレベルで試しにくい
2. 毎回コンパイルを必要とする

という点ですが、書いてすぐ試せるって良くないですか？  
これがスクリプト言語である利点です。  
書き捨てのコードや簡単なツールを用意する上でこの要件は外せないはずです。

### シンプルで読みやすい

Python はシンプルであるよう設計された言語で、コード哲学が **一つのことには一つのやり方を** という考え方があります。  
これは、誰が書いても究極的に単一のやり方にすべきだといった哲学があり、Perl/Ruby の「多様性は善」とは対照的です。

とはいえ、支配的な訳ではありません。これをもって毛嫌いする方が稀に居ますがご心配なく。  
Python は徹底した **シンプル** さが最大の善とされます（コミュニティもこの傾向です）。

これらは **誰が書いても似たような書き方に、誰もが同質の可読性を**

という点に繋がります。これはスクリプトを誰かが書いても続きを保守しやすいってことですよね。

言語仕様がそもそもシンプルなので、予約語数を比較すると、どれだけ習得が楽なのかがわかります。

[ゼロイチ「Ruby、PHP、Python、Javaの予約語の一覧」](https://programming-beginner-zeroichi.jp/articles/53)

Python はわずか 32、比較対象として Java なら 50 この差！

### ライブラリが強力でしかも使いやすい

Python のライブラリは非常に強力です。後述しますが、標準だけでも HTTP どころか Web サーバが数行で行きます。  
そして私の知る数少ない **ドキュメントをインタプリタから参照する言語仕様を持つ言語** です。

help 関数なんてものが存在しており、関数の先頭に書いたドキュメントを表示する機能です。  
ググる必要？よほど応用したいか探したい時だけどうぞ。

```python
>>> import io
>>> help(io)
Help on module io:

NAME
    io

MODULE REFERENCE
    https://docs.python.org/3.7/library/io

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    The io module provides the Python interfaces to stream handling. The
    builtin open function is defined in this module.

    At the top of the I/O hierarchy...
```

### データサイエンス（+AI）では R と共に支配的

Python が最近よく目につく理由は特にこれです。  
**AI 系ライブラリが整っていて、他言語の追随を許さない**

私はデータサイエンスは勉強中のアマチュアですが、プロでも理論検証にはまず Python を使うことが多いそうです。  
それはなぜか？

**汎用言語でありながら、データサイエンスが簡単にできるから**

この一点に尽きます。

## 目次

どうです？第二言語として手を伸ばしてみるのも良いのではないでしょうか？  
以下全部チュートリアルです。

1. [Python インストール](1.install/README.md)
2. [チュートリアル](2.tutorial/README.md)
3. [ファイル操作(ログ解析など)](3.usefiles/file/README.md)
4. [XML の操作](3.usefiles/xml/README.md)
5. [CSV の IO](3.usefiles/csv/README.md)
6. [Excel の IO](3.usefiles/excel/README.md)
7. [シェルとの共存](4.useshell/README.md)
8. [瞬間 HTTP サーバ](5.servers/http_server/README.md)
9. [RESTサーバを数行で！](5.servers/rest_server/README.md)
10. [Webクライアント](6.web_client/README.md)
11. [テストライブラリ](7.tests/unittest/README.md)
12. [Web負荷テストを簡単に](7.tests/stress_test/README.md)
13. [データ解析前夜(jupyter)](8.notebook/README.md)
14. [数学を手軽に](9.math/README.md)
15. [データ分析](10.data_analysis/) JupyterNotebook でご確認ください。
16. [機械学習の入り口(scikit-learn)](11.mechanical_learning/) JupyterNotebook でご確認ください。
17. [データサイエンス基礎](12.datascience/notebooks/) JupyterNotebook でご確認ください。
