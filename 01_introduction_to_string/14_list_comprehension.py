a = [1,2,3,4,5,6,7,8,9,10]

# General Method:
new_a = []

for i in a:
    if i % 2 == 0:
        new_a.append(i)
# print(new_a)

# where we can do same thing using comprehension in a efficient way:

#Comprehension Method: [expression for item in iterable if condition]
new_b = [i for i in a if i % 2 ==0]
print(new_a)
print(new_b)
#Both will be giving the same output
        