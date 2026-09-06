# { } is notation
#Unordered
#immutable = no update accepted
# No duplicates
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
z = set(a)
print(f"Listed items are: {a}")
print(f"Unique items are: {z}")

b = {1, 2, 3, 4}
c = {3, 4, 5, 6}
d = b.intersection(c)
e = b.union(c)
print(f"Intersection Result: {d}")
print(f"Union Result: {e}")