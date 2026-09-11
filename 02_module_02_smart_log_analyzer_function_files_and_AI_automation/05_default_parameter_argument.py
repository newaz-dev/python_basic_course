# This is the normal one.....
def print_my_name(f_name, l_name):
    print(f_name, l_name)

print_my_name("Newaz", "Fahmir")
# ==================================
# What if we just give single value "Newaz" ?

# then it will show us a mistake for the below line: 10 
# print_my_name("Newaz")
# line: 10 will be asking for another value for 'l_name'
# But if we just do the same thing with a default value, then the problem will be gone
def solution_function(f_name, l_name = "Khan"): #The preassigning value will work for missing value.. 
    print(f_name, l_name)

solution_function("Newaz", "Fahmir")
solution_function("Newaz")

def unknown_function():
    pass #Basically, When we dont know what to define
  
