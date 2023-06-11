class Node:

    def __init__(self, value, left=None, right=None, parent=None):
        self.__value = value
        self.left = left
        self.right = right
        self.parent = parent

    def get_value(self):
        return self.__value
    
    def append(self, node):
        if self < node:
            if self.left:
                self.left.append(node)
            else:
                node.parent = self
                self.left = node
        elif self > node:
            if self.right:
                self.right.append(node)
            else:
                node.parent = self
                self.right = node

        
    def __str__(self):
        return str(self.__value)

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.__value < other.get_value()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.__value > other.get_value()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.__value == other.get_value()
        return NotImplemented
