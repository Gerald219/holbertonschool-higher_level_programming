#!/usr/bin/python3
element_at = __import__('element_at_test').element_at

my_list = [1, 2, 3, 4, 5]

print("Element at index 3 is {}".format(element_at(my_list, 3)))
print("Element at index -1 is {}".format(element_at(my_list, -1)))
print("Element at index 10 is {}".format(element_at(my_list, 10)))
