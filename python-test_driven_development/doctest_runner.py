#!/usr/bin/python3
import importlib.util
import doctest

spec = importlib.util.spec_from_file_location("add_integer", "./0-add_integer.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

globals()["add_integer"] = module.add_integer

doctest.testfile("tests/0-add_integer.txt")