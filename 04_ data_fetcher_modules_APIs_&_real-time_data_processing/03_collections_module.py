import collections as c
# print(c.__doc__)

foods = ["rice", "beaf", "vegetables", "beaf", "meats", "beaf", "chicken", "vegetables", "eggs"]
print(c.Counter(foods))# for count fruits in dictionary
print(c.Counter(foods).most_common(2))# for count fruits in dictionary
