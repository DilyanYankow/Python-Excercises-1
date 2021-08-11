# str.format = optional method that gives users more control when displaying output
#
# animal = "Cow"
# item = "Moon"

# print("The " + animal + " landed on the " + item)
#
# print("The {} jumped over the {}.".format(animal, item))
#
# print("The {1} jumped over the {0}.".format(animal, item)) #positional argument
#
# print("The {animal} jumped over the {item}.".format(animal="cow", item="Moon"))
# print("The {item} jumped over the {item}.".format(animal="cow", item="Moon"))
# print("The {item} jumped over the {animal}.".format(animal="cow", item="Moon"))
#
# animal = "Cow"
# item = "Moon"
# text = "The {} jumped over the {}"
# print(text.format(animal, item))


name = "Dinzo"

# print("My name is {:}".format(name))
# print("My name is {:10}".format(name))
# print("My name is {:<10}. Nice to meet you".format(name))
# print("My name is {:^10}. Nice to meet you".format(name))
# print("My name is {:>10}. Nice to meet you".format(name))
print("My name is {name:10}. Nice to meet you".format(name="Dinzo"))

number = 3.14159
print("The Pi is {:.2f}".format(number))    #f for float, will round your number
number2 = 12345

print("The number is {:,}".format(number2))
print("The number is {:b}".format(number2))     #2bit
print("The number is {:0}".format(number2))     #8bit
print("The number is {:x}".format(number2))     #16bit
print("The number is {:E}".format(number2))     #scientific