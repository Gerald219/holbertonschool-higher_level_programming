from task_03_xml import serialize_to_xml, deserialize_from_xml

# Sample dictionary
sample_dict = {
    'name': 'John',
    'age': '28',
    'city': 'New York'
}

# File to save XML
xml_file = "data.xml"

# Serialize the dictionary to XML
serialize_to_xml(sample_dict, xml_file)
print(f"Dictionary serialized to {xml_file}")

# Deserialize back to a dictionary
loaded_data = deserialize_from_xml(xml_file)
print("\nDeserialized Data:")
print(loaded_data)
