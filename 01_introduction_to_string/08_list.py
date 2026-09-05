#Expression with Items
list = ["apple", "banana", "cherry", 1, 2, 3.4]
print(list)
print(list[1]) # to access the second item of the list
list[1] = "blackcurrant"
print(list)
list.append("orange") # To insert new item to the list
list.insert(3, "mango") # To insert new item to the list at specific position
print(list)
list.remove("apple") # To removeitem from the list
print(list)
list.pop(5) #To remove 6th item: 3.4 from list
print(list)
list.pop()
print(list)
del list[0]
print(list)
del list
print(f"Items are: {list}")
