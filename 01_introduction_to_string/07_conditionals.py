# # #One task is dependent on another task

# # # eg: 
# # # if it's raining,
# # #         Don't go outside.
# # # else, Go outside.

# # Let's have an example to understand this proble and solution:
# x = int(input("Enter any number you want to know its type: "))

# if x<0:
#     print("It's a Negetive number.")
# else:
#     print("Positive Number.")

# # Let's say you have multiple conditions to check...what to do then?
# # =======Introducing ELIF keyword=========#


# ####Problem####
# #Take input a, b, and c from user. Find the greatest numbber.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b:
    if a > c:
        print("1st number is greater")
elif b > c:
    print("2nd number is greater")
else:
    print("3rd number is greater")
    