# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments
import kwargs as kwargs


def hello(**names):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in names.items():
       print(value, end= " ")


hello(first="first1", middle="second2", last="last3")