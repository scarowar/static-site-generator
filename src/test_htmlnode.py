import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        html = node.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com" target="_blank"')

    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_eq_tags(self):
        node = HTMLNode(tag="p", value="Hello World")
        node2 = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
