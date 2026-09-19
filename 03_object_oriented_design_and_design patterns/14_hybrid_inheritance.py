# Person --> Student and  Person --> Employee = Hierarchical inheritance
# Student + Employee --> TeachingAssistant = Multiple inheritance
# Hierarchical inheritance + Multiple inheritance = Hybrid inheritance
class Person:
    def person_info(self):
        print("I am a person")


class Student(Person):
    def student_info(self):
        print("I am a student")


class Employee(Person):
    def employee_info(self):
        print("I am an employee")


class TeachingAssistant(Student, Employee):
    def assistant_info(self):
        print("I am a teaching assistant")


ta1 = TeachingAssistant()

ta1.person_info()
ta1.student_info()
ta1.employee_info()
ta1.assistant_info()
