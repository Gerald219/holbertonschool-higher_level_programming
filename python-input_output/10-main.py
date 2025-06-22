#!/usr/bin/python3
Student = __import__('10-student').Student

student = Student("John", "Doe", 23)

# No filter - should return all attributes
print(student.to_json())

# Filtered attributes - should return only first_name and age
print(student.to_json(['first_name', 'age']))

# Attributes that don't all exist - should ignore non-existent
print(student.to_json(['middle_name', 'age']))
