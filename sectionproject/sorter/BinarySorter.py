'''
Created on Oct 23, 2012

@author: hunlan
'''
from sectionproject.sorter.Sorter import Sorter

class BinarySorter(Sorter):
    @staticmethod
    def sort(urls):
        node = _Node(urls.pop())
        for url in urls:
            node.insert(url)
            
        return node.getSorted()
    
class _Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data
    
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = _Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = _Node(data)
            else:
                self.right.insert(data)
                
    def getSorted(self):
        ret = []
        if self.left:
            ret.extend(self.left.getSorted())
        ret.append(self.data)
        if self.right:
            ret.extend(self.right.getSorted())
        return ret