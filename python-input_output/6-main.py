#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# file we saved earlier in task 5
filename = "saved_data.json"

# load the data back from the file
data = load_from_json_file(filename)

# print what we got to make sure it worked
print("Loaded data:", data)
print("Type:", type(data))
