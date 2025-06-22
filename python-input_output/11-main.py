#!/usr/bin/python3
Student = __import__('11-student').Student

student_1 = Student("John", "Doe", 23)
print(student_1.__dict__)

student_2 = Student("Bob", "Dylan", 27)
print(student_2.__dict__)

json = student_2.to_json()
student_1.reload_from_json(json)
print(student_1.__dict__)
print(student_2.__dict__)
