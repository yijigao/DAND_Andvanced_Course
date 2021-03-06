import xml.etree.cElementTree as ET
import pprint


OSMFILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"
OSM_File = "C:\\Users\\yijig\\Desktop\\Advanced course\\sample.osm"

def is_bank(element):
    for tag in element.iter("tag"):
        if tag.attrib['k'] == "amenity":
            return tag.attrib['v'] == "bank"

for event,element in ET.iterparse(OSMFILE,events=("start",)):
    if is_bank(element):
        for tag in element.iter("tag"):
            if tag.attrib['k'] == "name":
                pprint.pprint(tag.attrib["v"])