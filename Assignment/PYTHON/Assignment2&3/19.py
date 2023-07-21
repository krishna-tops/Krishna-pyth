#first to take a new  default list list
lis1 = [25,"python",36,"java",67,"script"]
#then covert the list into ser
lis2 = set(lis1)
#then covert the set into list to get unique elements
list2 = list(lis2)
#finally print the list
print("Unique elements of a list",list2[2])
