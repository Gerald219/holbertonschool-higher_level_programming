#!/usr/bin/python3
print("✅ 1-main.py is running")
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 2, 4, 2, 5]
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)
