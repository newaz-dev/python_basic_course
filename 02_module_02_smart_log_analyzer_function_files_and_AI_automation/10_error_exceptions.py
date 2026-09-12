# First what is compile time and run time?

# 1. Compile-time Error:
# An error detected before the program runs, usually caused by incorrect syntax.
# print("Hello"  # Missing closing bracket
# Python won’t start the program.

# 2. Runtime Error:
# An error that occurs while the program is running.
# a = 10
# b = 0
# print(a / b)  # ZeroDivisionError
# The program starts, but crashes during execution.

# so we will do: Try and Catch
#Without try catch block this part(line:17 and 18) will not work cause the file not exist
# with open('name.txt', 'r') as f:
#     print(f.read())

#With try catch block this part will not work cause the file not exist but dont give any error
import os
import pathlib

try: #in the block of code where may be have some errors:
    with open("name.txt", 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found.")
#So this was the very basic concept
#Again: 
try:
    # with open("name.txt", 'r') as f:
    #     print(f.read())
    # print(10/0)
    x = int(10)
    print(x)
    z = [1,2,34]
    print(z[100])
# except FileNotFoundError:
#     print("File Not Found.")
except ZeroDivisionError:
    print("Dividing with 0 is not possible")
except ValueError:
    print("Invalid Value")
except Exception as e:
    print("some error occured in: ", e)
else:
    print("Code executed successfully")
finally: 
    print("this will must run ....")


#Custom Error Creation:
def check_file(file_name):
    if not file_name.endswith('.txt'):
        raise ValueError("Only .txt files are accepted") #We manually create exception with 'raise ' keyword



#CUSTOM ERROR EXCEPTION HANDLING:

try: 
    check_file("file_name.csv")
except Exception as e: 
    print(e)
