#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

# Example JSON text (as string)
my_str = '{"name": "Gerald", "age": 26, "languages": ["Python", "SQL", "HTML"]}'

# Convert JSON string back into Python data
python_obj = from_json_string(my_str)

print(python_obj)
print(type(python_obj))
