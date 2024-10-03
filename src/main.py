from parentnode import ParentNode
from leafnode import LeafNode

def main():
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

    print(section.to_html())

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

if __name__ == "__main__":
    main()
