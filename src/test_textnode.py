import unittest

from textnode import (
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
    TEXT_TYPE_LINK,
    TEXT_TYPE_IMAGE,
    text_node_to_html_node,
    )


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD)
        node2 = TextNode("This is a text node", TEXT_TYPE_BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr_with_url(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://example.com)")

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example.com")
        self.assertEqual(node, node2)

    def test_eq_with_different_url(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example2.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example.com")
        node2 = TextNode("This is a text node2", TEXT_TYPE_BOLD, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TEXT_TYPE_ITALIC, "https://example.com")
        self.assertNotEqual(node, node2)


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is a text node", TEXT_TYPE_TEXT)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), "This is a text node")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is a text node", TEXT_TYPE_BOLD)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), "<b>This is a text node</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is a text node", TEXT_TYPE_ITALIC)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), "<i>This is a text node</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is a text node", TEXT_TYPE_CODE)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), "<code>This is a text node</code>")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("This is a text node", TEXT_TYPE_LINK, "https://example.com")
        self.assertEqual(text_node_to_html_node(text_node).to_html(), '<a href="https://example.com">This is a text node</a>')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("This is a text node", TEXT_TYPE_IMAGE, "https://example.com")
        self.assertEqual(text_node_to_html_node(text_node).to_html(), '<img src="https://example.com" alt="This is a text node">')

    def test_text_node_to_html_node_invalid(self):
        text_node = TextNode("This is a text node", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
