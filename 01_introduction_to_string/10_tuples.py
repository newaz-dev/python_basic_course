t = ("apple", "banana", "cherry")#Its a tuple 
print(t[1])

# We cannot change tuple directly, for that we want help from list
x = ("apple", "mango", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Tuple Joining
tuple3 = t + x
print(tuple3)
print(tuple3.count(5))
