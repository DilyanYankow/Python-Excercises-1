#dictionary = key+values
#fast cuz they use hashing
capitals = {'USA':'Washington DC', "Bulgaria":"Sofia", "Turkey": "Istanbul"}

capitals.update({"Germany": "Berlin"})
capitals.update({"Germany": "Las Vegas"})

capitals.pop("Turkey")
#capitals.clear()    #removes all items
# print(capitals['USA'])    #bad practice, causes Error when none

print(capitals.get('Bulgaria'))     #returns "None" if nothing found
print(capitals.keys())      #returns all the keys
print(capitals.values())    #returns all the values only
print(capitals.items())     #returns values and keys


for key, value in capitals.items():
    print(key, value)