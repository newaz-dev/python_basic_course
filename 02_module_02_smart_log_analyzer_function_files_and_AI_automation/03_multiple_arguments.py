def addition(*args):# we can pass parameters as much we want 
    print(args) # it will print a tuple of having parameters from function call
    return sum(args)

result = addition(1, 2, 3, 4, 5) #Pass multiple parameters
print(result)