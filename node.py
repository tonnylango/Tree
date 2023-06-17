from functools import total_ordering

#TODO : able to search up from a node.

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
    
    #below code still in production
    #join a node; remove dublicates
    def _join(self, node):
            pass


    def remove(self):
        node = self.right or self.left

        if node:
            if self.right and self.left:
                node.append_node(self.left)

            if self.parent:
                self.parent.append_node(node)
            else:
                node.parent = None

        else:
            if self.parent:
                if self > self.parent:
                    self.parent.right = None
                else:
                    self.parent.left = None

        self.parent = None
        self.left = None
        self.right = None
        self.__value = None

        del self

        return node
        

        

    def path(self, value):
        root = self
        value = Node(value)
        path_list = []

        while root and root != value:
            path_list.append(root.get_value())
            root = root.left if root > value else root.right


        if root == value:
            path_list.append(value.get_value())
            return path_list
        else:
            return []
        
    def find_distance(self, value):
        lca = self.find_lca(value)
        return len(lca.path(value)) - 1 + len(lca.path(self.__value)) - 1 if lca else 0
    
    #find least common ancestor
    def find_lca(self, value):
        lca = self

        while lca and not lca.path(value):
            lca = lca.parent

        return lca

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
    
    def search(self, node):
        root = self
        node = Node(node)

        while root and root != node:
            root = root.left if root > node else root.right

        return root
    
    def structure(self):
        lines = []
        lines.append(f"  {self.parent or ' '}")
        lines.append("  |")
        lines.append(f"  {self}")
        lines.append(" / \\")
        lines.append(f"{self.left or ' '}   {self.right or ' '}")
        return str("\n".join(lines))


    
def inorder(root: Node) -> list:
    if root:
        left_subtree = inorder(root.left)
        right_subtree = inorder(root.right)
        left_subtree.extend([root.get_value()])  # Extend the left subtree list with the current node value
        left_subtree.extend(right_subtree)  # Extend the combined left subtree list with the right subtree list
        return left_subtree
    return []

def preorder(root: Node) -> list:
    if root:
        left_subtree = preorder(root.left)
        right_subtree = preorder(root.right)
        return [root.get_value()] + left_subtree + right_subtree
    return []

def postorder(root: Node) -> list:
    if root:
        left_subtree = postorder(root.left)
        right_subtree = postorder(root.right)
        return left_subtree + right_subtree + [root.get_value()]
    return []

