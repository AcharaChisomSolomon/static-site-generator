class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.__tag = tag
        self.__value = value
        self.__children = children
        self.__props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return ' ' + " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.__tag}, {self.__value}, {self.__children}, {self.__props})"