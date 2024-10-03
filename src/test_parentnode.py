import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_only_leafnodes_as_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_parentnode_as_children(self):
        another_div = ParentNode("div", [
            LeafNode("p", "Hello, World!"),
            LeafNode("p", "This is a paragraph.")
        ])
        div = ParentNode("div", [
            LeafNode("p", "Hello, World!"),
            LeafNode("p", "This is a paragraph.")
        ])
        section = ParentNode("section", [
            div,
            another_div
        ])

        self.assertEqual(
            section.to_html(),
            "<section><div><p>Hello, World!</p><p>This is a paragraph.</p></div><div><p>Hello, World!</p><p>This is a paragraph.</p></div></section>",
        )

    def test_to_html_with_parentnodes_and_leafnodes_as_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "span",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b><span>Normal text<i>italic text</i>Normal text</span></p>",
        )

    def test_to_html_with_parentnodes_and_prop(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "span",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
            {"class": "paragraph"},
        )

        self.assertEqual(
            node.to_html(),
            '<p class="paragraph"><b>Bold text</b><span>Normal text<i>italic text</i>Normal text</span></p>',
        )

    def test_to_html_with_no_children_and_no_tag(self):
        node = ParentNode()

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_no_children(self):
        node = ParentNode("p")

        with self.assertRaises(ValueError):
            node.to_html()

