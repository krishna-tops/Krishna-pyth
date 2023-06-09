# first we take input from user of both lists upto 5th element(included 5th element)
for i in range(0,2):
    l1= input("Enter a list: ")
for i in range(0,2):
    l2= input("Enter a sublist: ")
#convert in to list
list1 = list(l1)
list2 = list(l2)
#then took count as a 0 default
count = 0
#make a condition that elements of lists having in other list and print it 
if l1 in l2:
    print("yes,Element of list having in sublist")
else:
    print("no,Element of list having in sublist")




