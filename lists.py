

food = ["pizza", "eggs", "chicken"]

food[0]="is this 0?"    #update



food.append("new item added to end of list")
food.remove("is this 0?")
food.pop()      #removes last item
food.insert(0,"cake")
food.sort()         #sorts alphabettically

for i in food:
    print(i)

food.clear()    #deletes every item


