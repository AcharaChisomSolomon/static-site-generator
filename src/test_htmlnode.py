import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    node_1 = HTMLNode(
        "div", 
        "practice", 
        None, 
        {"class": "container", "id": "main", "style": "background-color: white"})
    node_2 = HTMLNode("p", "hello", None, {"class": "text"})

    def test_props_to_html(self):
        self.assertEqual(
            self.node_1.props_to_html(), 
            ' class="container" id="main" style="background-color: white"')
        self.assertEqual(self.node_2.props_to_html(), ' class="text"')

    def test_repr(self):
        self.assertEqual(
            repr(self.node_1), 
            "HTMLNode(div, practice, None, {'class': 'container', 'id': 'main', 'style': 'background-color: white'})")
        self.assertEqual(
            repr(self.node_2), "HTMLNode(p, hello, None, {'class': 'text'})")
        