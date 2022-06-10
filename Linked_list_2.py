from __future__ import annotations
from concurrent.futures import Future
from dataclasses import dataclass
from typing import Any

from more_itertools import last


class Node(object):
    def __init__(self,data:Any,next_data:Node) -> None:
        self.data = data
        self.next = next_data

class Linked_list():
    def __init__(self,head = None) -> None:
        self.head = head
    
    def append(self,data:Any) -> None:
        new_node = Node(data)
        if self.head == None:
            return 
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            return 
    
    def insert(self,data:Any) -> None:
        new_node = Node(data)
        self.next = self.head
        self.head = new_node
        return
    
    def remove(self,data:Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:

            
        