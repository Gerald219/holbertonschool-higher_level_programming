#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_saved.json"
data = load_from_json_file(filename)
print(data)
print(type(data))
