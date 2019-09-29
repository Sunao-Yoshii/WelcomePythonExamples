# 昔はファイルのエンコーディングを先頭に書きましたが、Python3 は UTF-8 が原則なので、不要になりました。
# output.py の中身

class Simplly:
    def __init__(self, name: str):
        self.__name = name

    def name(self):
        return self.__name
