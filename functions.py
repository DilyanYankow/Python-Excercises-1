# function = block of code, only executed when its called

def hello(name, lname, num):
    print("hello " + name + lname)
    print("Some int here: " + str(num))

# hello("Some name")
name = "Some name"
some_name = "other name"
# hello(some_name)
# hello(name)
age = 21
hello(name, some_name, age)

