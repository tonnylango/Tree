from node import Node

class Tree:
    #take a list of elements, convert them to nodes and connect them
    def __init__(self, values:iter=[]):
        self.__root #stores the root node
        self.__count = 0 #stores number of node
        #TODO convert to for each

        #if not values:
        #   raise ValueError("Values cannot be empty")
        if not isinstance(value, iter):
            raise ValueError("Invalid argument type. Expected an iterable object.")
        else:
            for value in values:
                self.insert(value)      
    
    def get_root(self):
        return self.__root

    #insert the node into the tree
    def insert(self, data):
        if not self.__root: #root is not set
            self.__root = Node(data)
        else:
            self.__root.append(data)

        self.__count += 1

    #returns the number of edges from the root node to that particular node
    def depth(self, node, from_node=None) -> int:
        from_node = from_node or self.__root

    #Check if an item is contained in the tree
    def __contains__(self, item) :
        pass 

    #delete the node from the tree
    def remove(self, value):
        pass

    #check if the value exist in the tree
    def search(self, node) -> Node:
        pass

    #count total number of nodes
    def __len__(self):
        return self.__count

    #return a sorted iterator
    def __iter__(self):
        pass