# Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns 
# those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. 
# For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be 
# those tags whose attributes are class="url" si name="url-form" si data-id="item".

import xml.etree.ElementTree as ET

def get_elements(path, attrs):
    tree = ET.parse(path)
    root = tree.getroot()
    elements = []
    for element in root.iter():
        if element.attrib == attrs:
            elements.append(element)
    return elements


def main():
    path = input('Enter path: ')
    attrs = input('Enter attrs: ')
    elements = get_elements(path, attrs)
    print(elements)

main()