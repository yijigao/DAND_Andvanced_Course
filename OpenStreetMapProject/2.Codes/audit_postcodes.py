import xml.etree.cElementTree as ET
import pprint


OSMFILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"

def audit_postcode(postcode):
    # 如果邮编是‘028’，将其转为成都市邮编‘610000’
    if postcode.startswith('028'):
        return '610000'
    else:
        return postcode

post_code = []
for event,element in ET.iterparse(OSMFILE,events=("start",)):
        for tag in element.iter("tag"):
            if tag.attrib['k'] == "addr:postcode":
                post_code.append(audit_postcode(tag.attrib['v']))

pprint.pprint(post_code)
