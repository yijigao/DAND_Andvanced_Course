import xml.etree.cElementTree as ET
import pprint


OSMFILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"

def audit_city(city_name):
    # 如果city_name不是是‘成都市’，将其转为‘成都市’
    if city_name != "成都市":
        return '成都市'
    else:
        return city_name

city_name = []
for event,element in ET.iterparse(OSMFILE,events=("start",)):
        for tag in element.iter("tag"):
            if tag.attrib['k'] == "addr:city":
                # print(tag.attrib['v'])
                city_name.append(audit_city(tag.attrib['v']))

pprint.pprint(city_name)