import xml.etree.ElementTree as ET

tree = ET.parse("product.xml")
root = tree.getroot()

print("root tag:", root.tag)

for p in root.iter('product'):
    print(p.tag)

for p in root.findall('product'):
    print(p.tag)
