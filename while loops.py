
#
# while 1==1:
#     print("Im stuck in a loop")

# name=""
# while len(name) == 0:
#     name = str(input("Enter your name: "))
#
# print("Hello " + name)

name = None
while not name:
    name = str(input("Enter your name: "))

print("Hello " + name)