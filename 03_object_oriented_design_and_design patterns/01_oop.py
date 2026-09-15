class Car:
        #__init__(): Dunder method. Constructor, no return
        # 3 Types 
# 1. Default Constractor
    def __init__(self): 
            self.brand = ""
            self.model = ""
# 2. Parameterized Constructor
    def __init__(self, brand, model): 
            self.brand = brand
            self.model = model
# 3. Default Value Constructor
    def __init__(self, brand = "Toyota", model = "Corolla"): 
            self.brand = brand
            self.model = model
#  Above here is a Default Constructor           
car1 = Car() #It will choose "Default Value Constructor"

car2 = Car() #It will choose "Default Constructor"
car2.brand = input("Enter Brand Name: ")
car2.model = input("Enter Models Name: ")

car3 = Car("x", "y") #It will choose "Parameterized Constructor"

print(car1.brand)
print(car1.model)

print(car2.brand)
print(car2.model)

print(car3.brand)
print(car3.model)