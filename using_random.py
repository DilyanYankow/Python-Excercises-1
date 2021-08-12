import random

x = random.randint(1, 6)
y = random.random()     #random number from 0 to 1

print(x)
print(y)

myList = ['rock', 'paper', 'scissors']

print("{random_choice}".format(random_choice=random.choice(myList)))

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(deck)
print(deck)

