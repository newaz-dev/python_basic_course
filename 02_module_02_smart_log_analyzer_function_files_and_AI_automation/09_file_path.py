import os
if os.path.exists('08.txt'):
    print("File found.")
else:
    print("File not found.")



import pathlib

file_path = pathlib.Path('08.txt')
if file_path.exists():
    print("File exists")
print(os.path.abspath("08.txt"))
print(os.path.getsize("08.txt"))

with open('08.txt', 'r') as f:
    print(f.tell())#It gives the cursior position
    print(f.read(5))#It will read 5 characters from the cursior position
    print(f.tell())#It gives the cursior position
