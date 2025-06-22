#!/usr/bin/python3
Student = __import__('9-student').Student

student = Student("John", "Doe", 23)
j_student = student.to_json()
print(type(j_student))
print(j_student)
