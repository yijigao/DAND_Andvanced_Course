import xml.etree.cElementTree as ET


for event, element in ET.iterparse("sample.osm",events=("start",)):
    if element.tag == "way" or element.tag == "node":
        for ele in element.iter("tag"):
            if ele.attrib["k"] == "addr:street":
                print(ele.attrib["v"])