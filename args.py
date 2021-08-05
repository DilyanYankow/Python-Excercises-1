#       *args

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

def add(*numbers):
    sum = 0
   # numbers = list(numbers)     #casted to list
   # numbers[2] = 100
    for i in numbers:
        sum += i
    return sum

print(add(1,2,3))