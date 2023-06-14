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
        if not isinstance(data, Node) and not isinstance(self.__value, Node): #if data is not a Node, make it a node
            if not isinstance(data, self.__value.__class__): #check if data is the same class as the current node value
                raise TypeError("Invalid data type. Expected instance of {}.".format(self.__value.__class__.__name__))
            else:
                data = Node(data)

        if self != data:
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
