import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leafnode_to_html_no_value(self):
        node = LeafNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leafnode_to_html_with_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting"})
        self.assertEqual(node.to_html(), '<p class="greeting">Hello, world!</p>')