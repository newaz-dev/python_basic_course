# dictionary = {value: key, value2: key2,........}
# must be having key value pair
# No indexing
# keys are immutable 
# Example:

a = {'shah': 1, 'newaz': 2, 'fahmir': 3, 'hridoy': 4, 5:[1, 2, 3, 4], 6:[3, 4, 5]}
print(type(a))
for i in a:
    print(i)
print("---------------------------") #segmenting 

for i in a.values():
    print(i)
print("---------------------------")

print(a.keys(), a.values())

print("---------------------------")

for k,v in a.items():
    print(f"Key name: {k}, Value: {v}")

print("---------------------------")

a = [1,2,3]
b = ["mango", "banana", "apple"]

c = zip(a, b)# it will give a tuple, but we need dictionary
d = dict(c)
print(d)