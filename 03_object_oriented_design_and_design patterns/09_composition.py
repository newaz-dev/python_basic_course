# Composition: Strong Relationship

class Engine:
    def __init__(self,power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)
    def show_details(self):
        print(f"{self.brand} car has a {self.engine.power} HP Engine")
car = Car("Tesla", 4000)
car.show_details()

