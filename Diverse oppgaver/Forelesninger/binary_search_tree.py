from tkinter.tix import Tree


class TreeNode:
    def __init__(self, object):
        self.element = object
        self.right = None
        self.left = None
        
        
class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__length = 0
        
        
    def insert(self, object):
        node = TreeNode(object)
        if seld.root ==