from multiprocessing.sharedctypes import Value


class Node(object):
    def __init__(self,value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node, value:int) -> Node:
    if node is None:
        return Node(value)
    
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    
    return node

def inorder(node: Node):    #２分木の要素を順番に一個ずつ表示
