import random as r
# help(random)
# print(dir(random)) <---- which proves, random is a module not package.
# We can do multiple things using Random Module
# Such as:
 
print(f"A random number is: {r.random()}") #This will give a random number each time between (0-1)
print(f"A random number between (5 - 10) is: {r.uniform(5,10)}") #This will give a random number each time between (5-10)
print(f"An Integer random number between (5 - 10) is: {r.randint(5,10)}")
print(f"A random number between is: {r.randrange(1, 100, 5)}")

foods = ["rice", "vegetables", "meats", "beaf", "chicken", "eggs"]
x = r.choice(foods)
print(x)

# for suffle foods 
r.shuffle(foods)
print(foods)


# For genetate random 4 digit pin

def genPin():
    return r.randint(1000, 9999)
print(f"Your four digit random pin is: {genPin()}")