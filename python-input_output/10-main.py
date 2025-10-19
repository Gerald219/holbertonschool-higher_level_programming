#!/usr/bin/python3
"""Quick test for 10-student"""


Student = __import__('10-student').Student


student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

print(student_1.to_json())
print(student_2.to_json(['first_name', 'age']))
print(student_2.to_json(['middle_name', 'age']))
