import unittest
from node import Node

class TestNode(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.node = Node(5)

    def test_get_value(self):
        self.assertEqual(self.node.get_value(), 5, "Get value is wrong")
    
    def test_initialize(self):
        #initialize with int, string
        int_node = Node(5)
        self.assertIsInstance(int_node.get_value(), int)
        self.assertEqual(int_node.get_value(), 5, "Get value int is wrong")

        str_node = Node("node")
        self.assertIsInstance(str_node.get_value(), str)
        self.assertEqual(str_node.get_value(), "node", "Get value str is wrong")

        list_node = Node([1,2,3])
        self.assertIsInstance(list_node.get_value(), list)
        self.assertEqual(list_node.get_value(), [1,2,3], "Get value list is wrong")

        class Test:
            pass

        test = Test()
        test_node = Node(test)
        self.assertIsInstance(test_node.get_value(), Test, "Get value Test class is wrong")

        node = Node(10)
        test_node = Node(node)
        self.assertIsInstance(test_node.get_value(), Node, "Get value Node is wrong")

    def test_append_small(self):
        #int
        node = Node(5)
        node.append(1)
        self.assertIsNotNone(node.left, "Left node should have small value int")
        self.assertIsNone(node.right, "Right node should be empty int")

        #node
        node.append(0)
        self.assertIsNotNone(node.left.left, "Left node should have small value int")
        #self.assertIsNone(node.get_right(), "Right node should be empty int")

    def test_append_big(self):
        #int
        node = Node(5)
        node.append(10)
        self.assertIsNotNone(node.right, "right node should have big value int")
        self.assertIsNone(node.left, "left node should be empty int")

        #node
        node.append(15)
        self.assertIsNotNone(node.right.right, "Left node should have small value int")
        #self.assertIsNone(node.get_right(), "Right node should be empty int")
    
    def test_comparison(self):
        small = Node(0)
        medium = Node(5)
        big = Node(10)
        equal = Node(0)

        self.assertEqual(small, equal, "Equal comparison failed: small and equal should be equal")
        self.assertNotEqual(small, medium, "Not equal comparison failed: small and medium should not be equal")

        self.assertLess(small, medium, "Less than comparison failed: small should be less than medium")
        self.assertGreater(medium, small, "Greater than comparison failed: medium should be greater than small")

        self.assertLessEqual(small, medium, "Less than or equal comparison failed: small should be less than or equal to medium")
        self.assertGreaterEqual(medium, equal, "Greater than or equal comparison failed: medium should be greater than or equal to equal")
