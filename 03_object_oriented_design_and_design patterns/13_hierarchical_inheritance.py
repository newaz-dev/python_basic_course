class Vehicle:
    def engine(self):
        print("The vehicle has a powerful Engine")

class Car(Vehicle):
    def quality(self):
        print("Car normaly use for Travelling")

class Truck(Vehicle):
    def capasity(self):
        print("A truck has a enormous capasity to carry")


car = Car()
truck = Truck()

car.quality()
car.engine()

truck.capasity()
truck.engine()
