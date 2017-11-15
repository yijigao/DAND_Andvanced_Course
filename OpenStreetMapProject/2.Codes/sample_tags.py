import re
import xml.etree.cElementTree as ET

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    if element.tag == "tag":
        streetname = element.attrib["k"]
        if re.search(lower, streetname):
            keys["lower"] += 1
        if re.search(lower_colon, streetname):
            keys["lower_colon"] += 1
        if re.search(problemchars, streetname):
            keys["problemchars"] += 1
        else:
            keys["other"] += 1
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for event, element in ET.iterparse(filename, events=("start",)):
        keys = key_type(element, keys)
    return keys

print(process_map("sample.osm"))