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
