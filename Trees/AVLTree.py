from AVLNode import AVLNode
from BinarySearchTree import BinarySearchTree
from BSTPrint import pretty_print
import random

class AVLTree (BinarySearchTree):


    def __init__(self):
        self._root = None

    def add(self, v):
        n = None
        if self.is_empty():
            n = AVLNode(v)
            self._root = n
        else:
            n = self._root.add(v)
            self._root = self._root.rebalance(v)
            self._root._parent = None
        return n

def avl_tree_test():
    tree = AVLTree()
    for i in range(12):
        new_value = random.randint(1, 99)
        print("Adding", new_value)
        tree.add(new_value)
        print(tree.list_in_order())
        print(tree.height())
        pretty_print(tree)

#avl_tree_test()