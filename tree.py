from node import *

class Tree:
    def __init__(self, values: iter = None):
        self.__root = None  # stores the root node
        self.__count = 0  # stores the number of nodes
        values = values if isinstance(values, (list, tuple, set, dict)) else iter([values])

        if values is not None:
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
    def distance(self, node, from_node=None) -> int:
        from_node = Node(from_node) if from_node else self.__root
        return from_node.find_distance(node)

    def path(self, data, root=None) -> list:
        root = Node(root) if root else self.__root
        return root.path(data)

    #Check if an item is contained in the tree
    def __contains__(self, item) -> bool:
        return bool(self.search(item) )

    #delete the node from the tree
    def remove(self, value):
        pass

    #check if the value exist in the tree
    def search(self, value) -> Node:
        return self.__root.search(value)
    
    #count total number of nodes
    def __len__(self):
        return self.__count

    #return a sorted iterator
    def __iter__(self):
        return iter(inorder(self.__root))