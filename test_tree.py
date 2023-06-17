import unittest
from node import Node
from tree import Tree

class TestTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.values = [5,2,3,6,7,10]
        cls.tree = Tree(cls.values)

    #def test_init(self):
    #    self.assertRaises(ValueError, Tree, [], "Expected ValueError to be raised for an empty list.")
    #    self.assertRaises(ValueError, Tree, 42, "Expected ValueError to be raised for an integer.")

    def test_path(self):
        self.assertEqual(self.tree.path(10), [5,6,7,10])

    def test_get_root(self):
        node = self.tree.get_root()
        self.assertEqual(node.get_value(), 5, "Root is not set ok")

    def test_contains(self):
        self.assertTrue(3 in self.tree, "Expected 3 to be in tree")
        self.assertFalse(4 in self.tree, "4 should not be in the tree")

    def test_count(self):
        self.assertEqual(len(self.tree), len(self.values), "Expected length to be the same size as list values")

    def test_depth(self):
        self.assertEqual(self.tree.depth(5), 0, 'root node should have a depth of 0')
        self.assertEqual(self.tree.depth(10, 6), self.tree.depth(6, 10), "Expected depth to be equal")

    def test_remove(self):
        self.tree.remove(10)
        self.assertFalse(10 in self.tree, "10 should have been removed")
        self.assertEqual(len(self.tree), len(self.values)-1, "Expected count to be the same size as list values minus one")

        #Remove node; root should be moved to another node
        root_node = self.tree.get_root()
        self.tree.remove(root_node.get_value())
        self.assertEqual(self.tree.get_root().get_value(), 6, "Root should have changed from 5 to 6")

        #remove value not in tree
        self.assertRaises(ValueError, self.tree.remove, 11, "Expected Value error for value not present")


    def test_search(self):
        node = self.tree.search(2)

        self.assertTrue(node, "2 should be in the tree")
        self.assertEqual(node.parent, self.tree.get_root(), "Parent of 2 should be the root")

        #self.assertRaises(ValueError, self.tree.search, 11, "Expected value error for value not present")

    def test_iter(self):
        tree_list = list(iter(self.tree))
        self.assertTrue(7 in tree_list, "Expected 7 in the tree list")