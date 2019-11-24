# XML の操作

for Python 3.7.x

## XML の標準的読み取り

Python3 には XML パーサが標準で存在します。  
そのサンプルをみながら話を進めます。

例題の XML はこんな値です。

```xml
<?xml version='1.0' encoding='utf-8'?>
<root>
    <title>技術をかじる猫</title>
    <sumamry>技術と名のつく物を気まぐれにかじるサイト</summary>
    <entry>
        <title>XML読み込み</title>
        <description>PythonでXMLを読み取るサンプル</description>
    </entry>
    <entry>
        <title>ファイルの読み書き</title>
        <description>ファイル操作は第二言語として必須でしょ？</description>
    </entry>
</root>
```

そしてこれを読み込んでみます。

```python
import xml.etree.ElementTree as ET

tree = ET.parse('./sample.xml')

title = tree.find('title').text
print(title)  # 技術をかじる猫

entry_titles = tree.findall('entry/title')
print([v.text for v in entry_titles])  # ['XML read in python', 'Dict read']
```

うーんシンプル

