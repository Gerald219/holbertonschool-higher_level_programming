#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

filename = "my_first_file.txt"
nb_characters_added = append_write(filename, "This School is absolutely amazing!\n")
print(nb_characters_added)
