#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("append_write", "2-append_write.py")
append_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(append_module)
append_write = append_module.append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
