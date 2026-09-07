txt = "Hello, I am Newaz, 25 years old."

# There are two method for formatting string
print(txt)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
#=========Method 1===========================
print("Hello, I am {name}, {age} years old.".format(name = name, age = age))
#============================================

#Both will be giving the same output

#=========Method 2===========================
print(f"Hello, I am {name}, {age} years old.")
#============================================
