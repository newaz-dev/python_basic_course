def key_word_func(f_name, l_name, age):
    print(f"\nHi, My name is {f_name} {l_name}. I am {age} years old. \n")

key_word_func("Newaz", "Fahmir", 25) # Order maintained
key_word_func("Fahmir", 25, "Newaz" ) # Order not maintained and it gives wrong result.
key_word_func(l_name = "Fahmir", age = 25, f_name = "Newaz" ) # Unordered Key_value defined parameter passed, gives exact output.

# Now if Arbitary number of arguments like below the line:10 then what to do?

# key_word_func(l_name = "Fahmir", age = 25, f_name = "Newaz", mark = 50, location = dhaka ) : This line will be generating error cause the parameters are not known to the function
# but the word '**kwargs' in func defination can handle it

def key_args_func(**kwargs):
    print(kwargs)
    print(f"\nHi, My name is {kwargs ['f_name']} {kwargs ['l_name']}. I am {kwargs ['age']} years old. I got {kwargs ['mark']} in programming and I live in {kwargs['location']} \n")
    print(f"\nHi, My name is {kwargs ['f_name']} {kwargs ['l_name']}. I am {kwargs ['age']} years old. \n")

key_args_func(l_name = "Fahmir", age = 25, f_name = "Newaz", mark = 50, location = "Dhaka" ) 
#RESULT: 


# Result of line:15: "Hi, My name is Newaz Fahmir. I am 25 years old. I got 50 in programming and I live in Dhaka"


# Result of line:16: Hi, My name is Newaz Fahmir. I am 25 years old. 

# but we pass same parameters you see!!!
