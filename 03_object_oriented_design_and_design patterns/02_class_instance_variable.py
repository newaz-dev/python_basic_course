class School:
    school_name = "Daffodil International University" # Class variable(always same)


    def __init__(self, name):
        self.studnet_name = name # Instance Variable(Unique for different objects)

sc1 = School("Newaz")
sc2 = School("Fahmir")
print(sc1.school_name)
print(sc1.studnet_name)
print(sc2.school_name, sc2.studnet_name)
School.school_name = "X" # From here every new object will have X school
sc3 = School("New Student")
print(sc3.school_name, sc3.studnet_name)
sc4 = School("4th Student")
print(sc4.school_name, sc4.studnet_name)
# If we just wanna change the name of school then 
