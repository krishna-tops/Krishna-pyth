number= []

# take 10 input from user
for i in range(10):
    n1= int(input("Enter number: "))
    number.append(n1)

#to find odd and even numbner
even_list = []
odd_list = []


for i in number:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)
new=[]
for i in number:
    if i in new:
        new.append(i)
