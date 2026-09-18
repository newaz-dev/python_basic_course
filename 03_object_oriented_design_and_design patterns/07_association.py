# This is just a simple Association between two classes
# It is very easier than it looks...
# First we will make two independent class that can intract between them
# Then we will make a method that can connect them inside one of those class
# Then simply call them....and thats it it is
# Lets do it:

# Student -Teacher: Association
# ================================
#Step1: 
class Student:
    def __init__(self, name):
        self.name = name
    #step3: Connection Method:
    def learn_from(self, teacher):
        print(f"{self.name} learn from {teacher.name}")
    #step: Extra:: 
class Teacher:
    def __init__(self, name):
        self.name = name
    def teacher_teaches(self):
        print(f"{self.name} is a good teacher")
#==============================
# =============================   
# Step2:    
student = Student("Newaz")
teacher = Teacher("Mr. Zayed")
# =============================

# Step4:
student.learn_from(teacher) #Connection between objects of 2 independent classes
# step: Extra
