#When called, a function will first use the local parameter then the global
#   Local > Enclosing > Global > Built-in


name = "Some global name"      #global scope, available inside and outside functions

def display_name():
    name = "Some local name"      #local scope, only inside this function
    print(name)


print(name)
display_name()
