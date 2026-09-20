# Polymorphism = Poly + Morphism
# Poly = Multi
# Morphism = Form 
# Polymorphism = Multiple Form 
# Basically two types
# 1. Method Override
# 2. Method Overloading

class Cat:
    def sound(self):
        print("Cat sounds: Meaw")

class Dog:
    def sound(self):
        print("Dog sounds: Woof")

cat = Cat()
dog = Dog()
# For both class sound() is a common form 
# but works differently 
cat.sound()
dog.sound()



# 1. Method Overriding:
class Grandfather:
    def height(self):
        print("Grandfather's height: 6 feet 2 inch")

class Father(Grandfather):
    def height(self):
        print("Father's height: 6 feet 0 inch")

class Child(Father):
    def height(self):
        print("Child's height: 5 feet 10 inch")

grandfather = Grandfather()
father = Father()
child = Child()

grandfather.height()
father.height()
child.height()

# The classes inherites Grandfather -->Father --> Child,
# So father.height() ---> should print("Grandfather's height: 6 feet 2 inch")
# Children class also should print the print("Grandfather's height: 6 feet 2 inch") same
# But for overriding they print their own funtions values.


# Method Overloading:
# In traditional way Python does not support Overloading
# java and C++ supprots is the Overloading Methods 