import xml.etree.cElementTree as ET

OSM_FILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\OpenStreetMap Project\\Chengdu.osm"
SAMPLE_FILE = "C:\\Users\\yijig\\Desktop\\Advanced course\\sample.osm"

k = 20 # take every k-th top level element
def get_element(osm_file, tags=("node","way","relation")):
    """
    Yield element if it is the right tag
    :param osm_file:
    :param tags:
    :return:
    """
    context = iter(ET.iterparse(osm_file,events=("start","end")))
    _,root = next(context)
    for event, element in context:
        if event == "end" and element.tag in tags:
            yield element
            root.clear()

with open(SAMPLE_FILE,"wb") as output:
    output.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    output.write(b"<osm>\n")

    # Write every kth top level element
    for i, element in enumerate(get_element(OSM_FILE)):
        if i % k == 0:
            output.write(ET.tostring(element,encoding='utf-8'))

    output.write(b"</osm>")
