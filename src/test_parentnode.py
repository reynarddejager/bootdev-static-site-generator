import unittest
from parentnode import ParentNode
from leafnode import LeafNode   

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_empty_tag(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("", [])
            parent_node.to_html()

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", [])
            parent_node.to_html()

    def test_to_html_with_properties(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>'
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild", {  "style": "font-weight: bold;"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b style="font-weight: bold;">grandchild</b></span></div>'
        )
               
if __name__ == "__main__":
    unittest.main()