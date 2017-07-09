#!/usr/bin/python3

import xml.etree.ElementTree as ET
tree = ET.parse('053.xml')
root = tree.getroot()
print(tree)
print(root)

