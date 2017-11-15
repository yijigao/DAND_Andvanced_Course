import xml.etree.cElementTree as ET



OSM_File = "C:\\Users\\yijig\\Desktop\\Advanced course\\sample.osm"

for event,element in ET.iterparse(OSM_File,events=("start=",)):
