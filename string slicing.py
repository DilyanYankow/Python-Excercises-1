name = "abcd efg hijkl"
#[start:stop:step]
#[inclusive:exclusive:exclusive?]
# first_name = name[0]
# print(first_name)
# #first_name = name[0:4]
# first_name = name[:4]
# print(first_name)
# last_name = name[5:len(name)+1]        #efg hijkl
# print(last_name)
# last_name = name[5:14]                 #efg hijkl
# print(last_name)
# last_name = name[5:]                   #efg hijkl
# print(last_name)
# last_name = name[5:14]                 #efg hijkl
# last_name = name[5:]                   #efg hijkl
# print(last_name)
# funky_name = name[::2]                 #ac f ik
# print(funky_name)
#
# reversed_name = name[::-1]               #lkjih gfe dcba
# print(reversed_name)

website1 = "http://google.com"
website2 = "http://facebook.com"
#-1 index is last symbol
slice_example = slice(7, -4)

print(website1[slice_example])                   #google

print(website2[slice_example])                   #facebook
