class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props    

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        if self.props:
            for k, v in self.props.items():
                result += f' {k}="{v}"'
        return result
    
    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props

    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"
