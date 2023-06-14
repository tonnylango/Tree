from node import Node

class Tree:
    #take a list of elements, convert them to nodes and connect them
    def __init__(self, values:list):
        self.__root #stores the root node
        self.__count = 0 #stores number of node
        #TODO convert to for each
        
        
    
    def get_root(self):
        return self.__root

    #insert the node into the tree
    def insert(self, value):
        node = Node(value)
        if not self._root: #if root is not set
            pass

    #returns the number of edges from the root node to that particular node
    def depth(self, value):
        pass

    #Check if an item is contained in the tree
    def __contains__(self, item):
        pass 

    #delete the node from the tree
    def remove(self, value):
        pass

    #check if the value exist in the tree
    def search(self, node):
        pass

    #count total number of nodes
    def count(self):
        pass

    #return a sorted iterator
    def __iter__(self):
        pass