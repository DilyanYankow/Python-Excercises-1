import os

path = "C:\\Users\\xdido\\Desktop\\UID.txt"

if (os.path.exists(path)):
    print("location exists")
    if(os.path.isfile(path)):
        print("That is a file")
    elif(os.path.isdir(path)):
        print("That is a directory")
else:
    print("location doesnt exist")

try:
    with open("UID.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found: ")