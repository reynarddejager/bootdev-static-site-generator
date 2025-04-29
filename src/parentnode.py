from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == "":
            raise ValueError("ParentNode must have a tag")
        
        if len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        
        html = f"<{self.tag}{self.props_to_html()}>"

        for node in self.children:
            html += node.to_html()

        html += f"</{self.tag}>"
        return html