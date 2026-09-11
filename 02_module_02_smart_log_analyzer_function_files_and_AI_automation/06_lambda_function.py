
import functools
#Its a anonymous Function--->Unnamed
def square(x):
    return x**2

print(square(5))

# Now the same thing can be done by lambda function easily
# Expression: lambda arguments : expression



square = lambda x: x*x #Defining 
y = square(20)#Calling
print(y)

add = lambda a, b: a + b
x = add(4,6)
print (x)

students = [('Rahim', 50), ('Raju', 60), ('Rabul', 55)]
sorted_students = sorted(students, key= lambda x: x[1])
print(sorted_students)

# Map(), Filter(), Reduce() using Lambda:

# Map()
# map(ki korte cacchi, kar upor apply korte cacchi)
numbs = [1,2,3,4,5]
#sq_numbers = list(map(ki korte cacchi, kar upor apply korte cacchi))
sq_numbers = list(map(lambda x: x*x, numbs))
print(sq_numbers)

#Filter(): Filter as required
even = filter(lambda x: x%2==0, numbs)
x = list(even) # to have a human readable format
print(x)

#Reduce(): Have to-->import functools
sum = functools.reduce(lambda x, y: x+y, numbs)
print(sum)