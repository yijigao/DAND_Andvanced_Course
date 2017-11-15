import csv
import codecs
import re
import xml.etree.cElementTree as ET
from collections import defaultdict


OSM_PATH = "Chengdu.osm"

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


street_type_re = re.compile(r'[路段街号道巷]$', re.IGNORECASE)
street_type_en_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "段", "街","路","号","巷","道","West","East","North","South"]

mapping = {"St":"Street",
           "St.":"Street",
           "st.":"Street",
           " st":" Street",
           "Rd":"Road",
           "Rd.":"Road",
           "Ave":"Avenue",
           "Ave.":"Avenue",
           "jie": "Street",
           "Jie": "Street"
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    n = street_type_en_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
    else:
        if n:
            street_type = n.group()
            if street_type not in expected:
                street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(element):
    street_types = defaultdict(set)
    if element.tag == "way" or element.tag == "node":
        for tag in element.iter("tag"):
            if is_street_name(tag):
                 audit_street_type(street_types, tag.attrib['v'])
    return street_types

def update_name(name, mapping):
    for key in mapping:
        if "," in name:
            name = name.split(",")[0]
            if name.endswith(key):
                return name.replace(key, mapping[key])
        if "-" in name:
            return name.split(" - ")[0]
        elif name.endswith(key):
            return name.replace(key, mapping[key])


def shape_tag(element,tag):
    tag = {
        "id": element.attrib['id'],
        "key": tag.attrib['k'],
        "value": tag.attrib['v'],
        "type": 'regular'
    }

    if tag["key"] == "addr:street":
        street_types = audit(element)
        for street_types,ways in street_types.items():
            for name in ways:
                tag["value"] = update_name(name, mapping)
    if LOWER_COLON.match(tag["key"]):
        tag["type"], _, tag["key"] = tag["key"].partition(":")

    return tag

def shape_way_node(element,i,nd):
    return {
        "id": element.attrib['id'],
        "node_id":nd.attrib['ref'],
        "position":i
    }

def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type="regular"):

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []

    tags = [shape_tag(element,t) for t in element.iter("tag")]

    if element.tag == "node":
        node_attribs = {f:element.attrib[f] for f in node_attr_fields}
        return {"node": node_attribs, "node_tags":tags}
    elif element.tag == "way":
        way_attribs = {f:element.attrib[f] for f in way_attr_fields}
        way_nodes = [shape_way_node(element,i,nd) for i,nd in enumerate(element.iter("nd"))]
        return {"way":way_attribs, "way_nodes": way_nodes,"way_tags":tags}

# ================================ #
#         Helper Functions         #
# ================================ #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()



class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v if isinstance(v,bytes) else v) for k, v in row.items()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

# ================================================== #
#               Main Function                        #
# ================================================== #

def process_map(file_in):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH,'w',encoding="utf-8") as nodes_file, \
            codecs.open(NODE_TAGS_PATH, 'w',encoding="utf-8") as nodes_tags_file, \
            codecs.open(WAYS_PATH, 'w',encoding="utf-8") as ways_file, \
            codecs.open(WAY_NODES_PATH, 'w',encoding="utf-8") as way_nodes_file, \
            codecs.open(WAY_TAGS_PATH, 'w',encoding="utf-8") as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()


        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])

if __name__ == '__main__':
    process_map(OSM_PATH)





