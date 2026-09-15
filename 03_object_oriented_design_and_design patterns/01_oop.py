class Car:
#__init__(): Dunder method. Constructor, no return
# 3 Types: 
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
# Instance Method:
    def display_info(self):
           print(f"Brand Name: {self.brand}, Model Name: {self.model}")
car1 = Car() #It will choose "Default Value Constructor"

car2 = Car() #It will choose "Default Constructor"
car2.brand = "Kawasaki"
car2.model = "Ninja H2R"

car3 = Car("x", "y") #It will choose "Parameterized Constructor"

# print(car1.brand)
# print(car1.model)

# print(car2.brand)
# print(car2.model)

# print(car3.brand)
# print(car3.model)

# Till now we have seen how we can print 
# using print function. But its not a good 
# Practice. So using instance we can do same
# using def display_info(self):

car1.display_info()
car2.display_info()
car3.display_info()

