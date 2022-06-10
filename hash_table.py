#辞書型とは　{(key_A:value_A),(key_B:value_B)} においてkeyとvalueを対応させるリスト形式


import hashlib
from typing import Any

class HashTable(object):    #ハッシュテーブルの作成cc

    def __init__(self, size = 10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)] #リスト内にリストがいくつもある    [[] [] [] [] []]


    def hash(self, key):        # [キー,値] => [車,トヨタ]
        return int(hashlib.md5(key.encode()).hexdigest(), base = 16)%10   # hashlib.md5(key.encode()).hexdigest() keyをエンコード（圧縮）して、16進数形式の文字列を取得する base = 16は16進数の値を10進数のint型にしたい時に用いる

    def add(self, key,value) -> None: #車のようなキーに対してトヨタのような値(value)を追加する
        index = self.hash(key)
        for data in self.table(index):  #data [車,トヨタ]　data[0]にキーが、data[1]にvalueが入る　keyとvalueは一対一対応
            if data[0] == key:
                data[1] = value
        else:
            self.table(index).append([key,value])
    
    def print(self) -> None:
        for index in range(self.size):
            print(index, end ='')  #end = ''は改行しないで表示したい場合に役立つ

            for data in self.table(index):
                print('-->', end= '')    #改行しない
                print(data, end='') #改行しない
            print() #最終的に改行したい時
    
    def get(self, key) -> Any:  #キーを与えて値を返す
        index = self.hash(key)
        for data in self.table(index):
            if key == data[0]:
                value = data[1]
        return value
        
if __name__ == '__main__':

