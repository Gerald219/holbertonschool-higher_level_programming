#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = '{ "is_active": true, "info": { "age": 36 } }'
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))
