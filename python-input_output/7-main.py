#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class_to_json = __import__('7-class_to_json').class_to_json

student = Student("John", "Doe", 23)
j_student = class_to_json(student)
print(type(j_student))
print(j_student)
