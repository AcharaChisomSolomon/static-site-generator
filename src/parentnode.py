from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def __get_child_html(self):
        html_str = ''

        for child in self.children:
            if isinstance(child, LeafNode):
                html_str += child.to_html()
            else:
                html_str += child.__get_child_html()

        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be set")
        if not self.children:
            raise ValueError("Children must be set")
        
        return self.__get_child_html()