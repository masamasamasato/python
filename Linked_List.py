#クラスの考え方 selfとは＝インスタンスそのものに値を代入するためのもの
#例えば name = nameとしてしまうとただの変数nameに値が代入されてしまう
#init 自動呼び出し

# class className():
#     def __init__(self, strA, strB) -> None: #この場合selfはクラスによって作られるインスタンス自身を表す。
#         self.strA = strA    #このインスタンスはstrAとstrBというカラムを持っているイメージ
#         self.strB = strB

# test = className("Hello","World")
# print(test.strA)
# print(test.strB)

# class Cat():
#     family = '猫'

#     def say(self):
#         print('にゃー')     #全てのインスタンスに共通している部分
    
#     def growl(self):
#         print('ウー')
    
#     def __init__(self, name) -> None:   #インスタンスごとに変えたい場合はinitを使うイメージ？
#         self.name = name
    

#連結リスト 非連結なリストの場合、最初にリストの長さを指定しなければならない。無駄に用意したり、足りなかったりする場合もある。ここで便利なのが連結リストというデータ構造

from __future__ import annotations
from cgi import print_environ_usage
from inspect import currentframe
from itertools import starmap
from re import L
from tkinter.messagebox import NO
from tracemalloc import start
from types import new_class #設定したNode型を変数のところの型として使いたい場合に用いる
from typing import Any


class Node(object): #ポインタの設定     Node('1') 1というデータの入ったオブジェクト 
    def __init__(self, data: Any, next_node:Node = None) -> None:   #dataは受け取り、next_dataは事前に設定されている
        self.data = data
        self.next = next_node

#n1 = Node('A') → ['A'|[ノード型] ]
#n2 = Node('B') → ['B'| ]


class Linked_list(object):  #関係性を表す（追加、削除などの関数の定義) linked_list内で定義した関数はlinked_list型のものに使える
    def __init__(self, head = None) -> None:    #イニシャライザ　インスタンスに初期値を与える　毎回作るインスタンスのhead自身は何もデータが入っていない
        self.head = head    #先頭ノード

#n1 = Linked_list() → head-[|] n1.append('A') → ['A'| ] 
#n1.append('B') → ['A'|['B' | ]]
    
    def append(self, data: Any) -> None:    #データの追加
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            last_node = self.head   #初期値みたいな
            while last_node.next:    # last_node.nextがNoneになるまでやり続ける
                last_node = last_node.next
            last_node.next = new_node
            return
    
    def insert(self, data: Any) -> None:    #先頭にデータを追加
        new_node = Node(data)
        new_node.next = self.head   #先頭ノード['A'|['B' | ]]を['C' | ]のnextに代入する
        self.head = new_node    #先頭ノードの更新
        return

    def remove(self, data: Any) -> None:    #要素の削除
        current_node = self.head
        if current_node and current_node.data == data:  #先頭にデータがあり、そのデータがdata
            self.head = current_node.next
            current_node.data = None
            return
        
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node == None:
            return
        
        previous_node.next = current_node.next
        current_node.data = None

        return
    
    def reverse_iterative(self) -> None:    #iterative = while文、for文を用いること
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next   #次のノードをnext_nodeに対比させておく
            current_node.next = previous_node

            previous_node = current_node    #previous_nodeの更新　上のやつと合わせてcurrent_node.nextが一個手前の要素であるprevious_nodeを挿すことがわかる
            current_node = next_node    #previous_nodeに対してcurrent_nodeが一個ずれる

        self.head = previous_node


    def reverse_recursive(self) -> None:    #再帰関数を用いた書き方
        def _reverse_recursive(current_node :Node, previous_node :Node) -> Node:

            if current_node == None:    #終了条件 ノードが何もない
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node,previous_node)  #再帰的に呼び出し
        
        self.head = _reverse_recursive(self.head,None)  #関数呼び出し

        # 1 4 6 8 9 => 1 8 6 4 9 偶数が連続して現れたらその部分だけひっくり返す　部分reverse
    def reverse_even(self) -> None:
        
        def _reverse_even(head: Node, previous_node: Node):
            
            if head == None:
                return None

            current_node = head     #[2,4,6,8]なら先頭の[2]がheadにあたる
        
            while current_node and (current_node.data%2) == 0:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            
            if current_node != head:    #while文に入った時
                head.next = current_node
                return previous_node
            
            else:   #まだwhile文に入っていない時
                head.next = _reverse_even(head.next,head)
                return head


        self.head = _reverse_even(self.head,None)   #先頭の更新


        # None->2->4->6  previous_node = [6->4->2->None]

        









        
        







# l = Linked_list()
#     l.append(1)
#     l.append(2)
#     l.insert(3)
#     print(l.head.data)
#     print(l.head.next.data)
#     print(l.head.next.next.data)  表示する時にめちゃくちゃ不便

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return

if __name__ == '__main__':
    l = Linked_list()
    l.append(1)
    l.append(2)
    l.append(4)
    l.append(6)
    l.append(3)
    l.print()
    print('###############')
    l.reverse_even()
    l.print()

    