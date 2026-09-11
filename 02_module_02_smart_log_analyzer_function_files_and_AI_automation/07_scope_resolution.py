# Scope is a region where a veriable is accessable
x = 10
y = 11
z = 12
def local():
    x = 30
    y = 40
    z = 50
    print("Inside local x is: ", x)
    print("Inside local y is: ", y)
    print("Inside local z is: ", z)
local()

print("Globally x is: ", x)
print("Globally y is: ", y)
print("Globally z is: ", z)

# To understand better  there is a keyword name: LEGB

# L = Local
# E = Enclosing
# G = Global
# B = Built in scope

#Example: 
n = "Global" #golobal veriable
def outer():
    n = "Enclosing"
    def inner():
        n = "Local"
        print(n)# this will print Local
    inner()
    print(n)# this will print Enclosing 
outer()
print(n)# this will print Global

print("============================================")

n = "Global" #golobal veriable
def outer():
    n = "Enclosing"
    def inner():
        global n # this will modify the "global" local 
        n = "Local"
        print(n)# this will print Local
    inner()
    print(n)# this will print Enclosing 
outer()
print(n)# this will print Global

print("============================================")

n = "Global" #golobal veriable
def outer():
    n = "Enclosing"
    def inner():
        nonlocal n # this will modify the "enclosing" to "local" 
        n = "Local"
        print(n)# this will print Local
    inner()
    print(n)# this will print Enclosing 
outer()
print(n)# this will print Global