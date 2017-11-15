import xml.etree.cElementTree as ET
import pprint



street = []
for event, element in ET.iterparse("Chengdu.osm",events=("start",)):
    if element.tag == "way" or element.tag == "node":
        for ele in element.iter("tag"):
            if ele.attrib["k"] == "addr:street":
                street.append(ele.attrib["v"])

pprint.pprint(street)