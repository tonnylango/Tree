from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, value):
        self.__value = value
        self.left = None
        self.right = None
        self.parent = None

    def get_value(self):
        return self.__value
        
    #append a data, value should be the same type
    def append(self, data):
        if not isinstance(data, type(self.__value)): #check if data is the same class as the current node value
            raise TypeError("Invalid data type. Expected instance of {}.".format(self.__value.__class__.__name__))
        
        if self != (data := Node(data)):
            self.append_node(data)

    
    def append_node(self, node):
        if node < self: #if self 
            if self.left:
                self.left.append_node(node)
            else:
                node.parent = self
                self.left = node
        elif node > self:
            if self.right:
                self.right.append_node(node)
            else:
                node.parent = self
                self.right = node

    def depth(self):
        if self is None:
            return 0

        #left_depth = self.left.tree_depth() if self.left else 0
        #right_depth = self.right.tree_depth() if self.right else 0
        
        #1 is added to it to account for the current level
        return max(Node.depth(self.left), Node.depth(self.right)) + 1

    def __hash__(self) -> int:
        return hash(self.__value)

        
    def __str__(self):
        return str(self.__value)
    
    def __repr__(self) -> str:
        return str(self.__value)

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.__value < other.get_value()
        return NotImplemented

    #def __gt__(self, other):
    #    if isinstance(other, Node):
    #       return self.__value > other.get_value()
    #   return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.__value == other.get_value()
        return NotImplemented
