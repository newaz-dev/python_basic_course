file = open('08.txt', 'r')#this is how we can read a file inside the same directory
content = file.read()
print (content)
file.close()

# But we can do the same with a easy alternative way
with open('08.txt', 'r') as f:
    content = f.read()
    print(content)

print("=============================================================")
# How to write in a file:

# This will overwrite the existing texts and update with the new code
with open("08.txt", 'w') as f:
    f.write("hello world\n")
    f.write("I am writing a new file")
# But all the time we dont need this...may be we want to add texts below the existing texts:
# Here append will help us:

with open("08.txt", 'a') as f:
    f.write("\nAfter using append:'a'\n")
    f.write("We got these lines here below hello world and I am writing a new file")

lines = ['\nI love  python', '\nI am new to python']

with open("08.txt", 'a') as f:
    f.writelines(lines)