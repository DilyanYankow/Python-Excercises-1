# exception, events detected during execution that interrupt the program

try:

    numerator = int(input("Enter a number to divide: "))
    denumerator = int(input("Enter a number to divide by: "))
    result = numerator / denumerator
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by 0")
except ValueError as e:
    print(e)
    print("Enter numbers only pls")
except Exception as e:
    print(e)
    print("Something went wrong, exception")
else:
    print(result)
finally:        #this will always execute
    print("YEP")