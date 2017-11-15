import xml.etree.cElementTree as ET
from collections import defaultdict
import pprint
import re



OSMFILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"

street_type_re = re.compile(r'[路段街号道巷]$', re.IGNORECASE) # 匹配最后一个汉字为“路段街号道巷”之一的街道名
street_type_en_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) # 匹配英文街道名空格后面的单词

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
    # 分别对英文和中文街道名进行处理
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

def audit(osmfile):
    with open(osmfile,"rb") as f:
        street_types = defaultdict(set)
        for event, elem in ET.iterparse(f, events=("start",)):
            if elem.tag == "way" or elem.tag == "node":
                for tag in elem.iter("tag"):
                    if is_street_name(tag):
                        audit_street_type(street_types, tag.attrib['v'])
        f.close()
    return street_types

def update_name(name, mapping):
    for key in mapping:
        # 对于有中英文混杂的名字，用“，”或“-”隔开，我们取中文名称
        if "," in name:
            name = name.split(",")[0]
            if name.endswith(key):
                return name.replace(key, mapping[key])
        if "-" in name:
            return name.split(" - ")[0]
        elif name.endswith(key):
            return name.replace(key, mapping[key])


def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = update_name(name, mapping)
            print(name, "=>", better_name)




if __name__ == '__main__':
    test()