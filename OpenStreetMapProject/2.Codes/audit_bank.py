import xml.etree.cElementTree as ET
import pprint
import re

OSMFILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"
OSM_File = "C:\\Users\\yijig\\Desktop\\Advanced course\\sample.osm"

bank_re = re.compile(r'[A-Z].*',re.IGNORECASE)

def is_bank(element):
    for tag in element.iter("tag"):
        if tag.attrib['k'] == "amenity":
            return tag.attrib['v'] == "bank"

for event,element in ET.iterparse(OSMFILE,events=("start",)):
    if is_bank(element):
        for tag in element.iter("tag"):
            if tag.attrib['k'] == "name":
                m = bank_re.search(tag.attrib['v'])
                if m:
                    pprint.pprint(m.group())
