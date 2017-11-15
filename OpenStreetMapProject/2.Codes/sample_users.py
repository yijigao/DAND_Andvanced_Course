import xml.etree.cElementTree as ET

def process_user(filename):
    users = set()
    for event, element in ET.iterparse(filename, events=("start",)):
        for ele in element.attrib:
            if "uid" in ele:
                if element.attrib["uid"] not in users:
                    users.add(element.attrib["uid"])
    return users

print(len(process_user("Chengdu.osm")))