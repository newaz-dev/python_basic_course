
#======= Type 01: No input, No return =============#

def my_first_function():  # function defination
    a = 10
    b = 15         # {This is Isolated Function with fixed value}
    print(a+b)

my_first_function()  #function call

#======= Type 02: Input, but no Return=============#
def add_two_number(x,y): # Argument passing function
    Sum = x+y
    print(Sum)

add_two_number(2,3)   # Function calling with parameters passing
add_two_number(4,6)   # Function calling with parameters passing


#======= Type 03:Input and Return =============#
def multiply_two_numbers(a,b):
    return a*b
result = multiply_two_numbers(10,2)
print(result)

#======= Type 04: No input, but return =============#
def hello():
    return "Hello"
greetings = hello()
print(greetings)