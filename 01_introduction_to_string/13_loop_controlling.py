list = [1, 2, 3, 4, 5, 'd', 6, 7, 8, 't', 'x', 9, 10]
for i in list:
    if type(i) == type("a"):
        break #this will stop the loop and take out from loop 
    else:
        print(i)
print("we are out from loop")

#Again

for i in list:
    if type(i) == type("a"):
        continue #this will ignore the item and continue the loop till end. 
    else:
        print(i)
print("Invalid items('d', 't', 'x') are excluded or ignored")
