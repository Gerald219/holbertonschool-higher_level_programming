#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "saved_data.json"
data = {"user": "Gerald", "age": 26, "skills": ["Python", "SQL", "HTML"]}

# this line calls your function and saves the data inside saved_data.json
save_to_json_file(data, filename)

print("Data saved to", filename)
