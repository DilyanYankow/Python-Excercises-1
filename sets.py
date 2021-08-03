#A set is unordered and unindexed. No dublicates

utensils = {"fork", "spoon", "knife", "knife"}      # with { }

dishes = {"bowl", "plate", "knife"}
#
# utensils.add("napkin")
# utensils.remove("fork")
# # utensils.clear()    #removes all items
#
# utensils.update(dishes)
# # dishes.update(utensils)
#
# dinner_table = utensils.union(dishes)
#
# for x in utensils:
#     print(x)    #only 1 knife is shown
#
print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))    #what they have in common
