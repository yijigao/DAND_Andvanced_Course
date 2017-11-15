import pprint
import xml.etree.cElementTree as ET

def count_tags(filename):
    tags = {}
    for event,elem in ET.iterparse(filename, events=("start",)):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags

pprint.pprint(count_tags("sample.osm"))