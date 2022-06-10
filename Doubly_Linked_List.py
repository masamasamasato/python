from __future__ import annotations
from os import preadv
from types import new_class
from typing import Any, Optional
from typing_extensions import Self

from sklearn.exceptions import NonBLASDotWarning

class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node
    
class Doubly_Linked_List(object):
    def __init__(self,head = None) -> None:
        self.head = head
    
    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        self.head.prev = new_node 
        new_node.next = self.head
    

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def remove(self, data: Any):
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return
        
        while current_node and current_node.data != data:
            current_node = current_node.next
        
        if current_node is None:    #どれにもヒットしなかった場合
            return
        
        if current_node.next is None:   #最後を削除する場合
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else:               #真ん中らへんを削除する場合
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    
    def reverse_iterative(self):
        previous_node = None
        current_node = self.head

        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node
            current_node = current_node.prev
            


            




        
        





