class Node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__root = None

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_root(self):
        return self.__root

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
