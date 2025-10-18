#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
my_dict = {'id': 12, 'name': "John"}

print(to_json_string(my_list))
print(type(to_json_string(my_list)))

print(to_json_string(my_dict))
print(type(to_json_string(my_dict)))
