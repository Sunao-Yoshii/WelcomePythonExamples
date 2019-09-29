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
