import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    
    def test_to_html_raises_exception(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_props_not_set(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_props_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_props_set(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph.", props={"class": "text"})
        self.assertEqual(repr(node), 'HTMLNode(p, This is a paragraph., None, {\'class\': \'text\'})')

if __name__ == "__main__":
    unittest.main()