#! usr/bin/env python
__author__ = 'Sandeep Kumar Nayak'
__status__ = 'development'
class Node():
    def __init__(self,value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def getHeight(self,root):
        if root == None:
            return -1
        else :
            left_height = self.getHeight(root.left_child)
            right_height = self.getHeight(root.right_child)

            return 1+max(left_height,right_height)
    #TODO: How to insert elements in a binary tree? Is it binary search tree or there
    # is any standard rule (like : left & right)
    def insert(self,value):
        if self.root:
            self.root = Node(value)
        else :
            pass
            # look both left & right
        pass

if __name__ == "__main__":

    arr = [3, 2, 5, 1, 4, 6, 7, 0, 8]
    root = Node()
    for num in arr:
        root.insert(num)

    print(root.getHeight(root))