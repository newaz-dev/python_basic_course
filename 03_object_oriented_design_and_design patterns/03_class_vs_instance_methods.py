class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Employee name: {self.name}\nSalary: {self.salary}")
    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name

object1 = Employee("Newaz", 100000) #Just making an object with some parameter
object1.display_info() #Call the instance method
Employee.change_company_name("Self Branding")
print(object1.company_name)

#ekhane bojhano hoiche kivabe and kokhon amra kon method ke call korbo....thats it
# #clas    @classmethod
#     def change_company_name(cls, name):
#         cls.company_name = name

# # code er ei part tuku hocche common...acceable from anywhere 
# and code er instance ba object part just object call 
# diye access possible