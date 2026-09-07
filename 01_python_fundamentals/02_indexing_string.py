s = "This is a string"
print(s[0])#output is T
print(s[15])#output is g

#print(s[16])#output is error

#so for last character printing we have some techniques
# 1. long way
print(s[len(s)-1])
# 2. short way
print(s[-1])
#both will give the same output