from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class

    @abstractmethod
    def start(self):  # Abstract method
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts using a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts using a self-starter")


car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()