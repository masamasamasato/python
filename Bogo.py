import random
#[式 for 任意の変数名 in イテラブルオブジェクト if 条件式] リスト内表記

def in_order(numbers: list) -> bool:  #型と返り値の指定が可能
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
        return True

def bogo_sort(numbers: list) -> list: #リストが正しく順序通りに並び変わっているかどうかを確認するのがbogo_sort()
    while not in_order(numbers): #繰り返し処理
        random.shuffle(numbers)
    return numbers

if __name__ == "__main__": #Bogo.pyがimportされた時にその場で実行されないようにする mainの場合だけ実行
    print(bogo_sort([1,5,7,3,2,4,6]))
