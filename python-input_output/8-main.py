#!/usr/bin/python3
class_to_json = __import__('8-class_to_json').class_to_json

class Student:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

student = Student("Gerald", 26, "Python")
print(class_to_json(student))
