z = [1,2,3,4,5]

result = 0
i = 0
n = len(z)
print("List elements are: ")
while i < n:
    result = result + z[i]
    print(z[i])
    i = i+1
print(f"Sum of the elements is: {result}")

# again 
i=0
while i < n:
    if z[i] % 2 != 0:
        z[i] = 0
    i = i + 1
print(z)
