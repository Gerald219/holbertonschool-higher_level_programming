#!/usr/bin/env python3
"""task 3 - xml serialize/deserialize."""


import xml.etree.ElementTree as ET  # module to build/read xml


def serialize_to_xml(dictionary, filename):
    """turn a dict into an xml file (overwrite filename)."""
    root = ET.Element("data")  # make <data> as the container
    for k, v in dictionary.items():  # loop each pair in the dict
        child = ET.SubElement(root, k)  # create a <key> tag
        child.text = str(v)  # put the value as text (xml is text)
    ET.ElementTree(root).write(  # save the xml to the file
        filename, encoding="utf-8", xml_declaration=True
    )


def deserialize_from_xml(filename):
    """read an xml file and return a dict (values come back as strings)."""
    tree = ET.parse(filename)  # open the xml file
    root = tree.getroot()  # get the <data> element
    out = {}  # start an empty dict
    for child in root:  # go through each child tag
        out[child.tag] = child.text  # tag name = key, text = value
    return out
