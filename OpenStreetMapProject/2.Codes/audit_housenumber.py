import xml.etree.cElementTree as ET
import pprint
import re


OSMFILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"

def audit_housenumber(house_number):
    """
    如果是数字的话，那就在后面加上“号”
    """
    try:
        if int(house_number):
            return house_number + "号"
    except ValueError:
        return house_number


house_number = []

for event,element in ET.iterparse(OSMFILE,events=("start",)):
        for tag in element.iter("tag"):
            if tag.attrib['k'] == "addr:housenumber":
                house_number.append(audit_housenumber(tag.attrib['v']))

pprint.pprint(house_number)