#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = [1, 2, 3]
my_dict = {
    'is_active': True,
    'info': {
        'age': 36,
        'skills': ['Python', 'C']
    }
}

save_to_json_file(my_list, "my_saved.json")
save_to_json_file(my_dict, "my_saved.json")
