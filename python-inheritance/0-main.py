#!/usr/bin/python3
lookup = __import__('0-lookup').lookup


class MyClass1(object):
    """Simple empty class"""
    pass


class MyClass2(object):
    """Class with one attribute and one method"""
    my_attr1 = 3

    def my_meth(self):
        """Dummy method"""
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
