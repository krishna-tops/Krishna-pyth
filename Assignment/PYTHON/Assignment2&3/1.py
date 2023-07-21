# to take a integer number from user
n = int(input("Enter a positive integer: "))

# make a loop for taking the number
sum = 0
for i in range(1, n+1):
    sum += i

# print the total of entered numbers 
print("The sum of the first", n, "positive integers is:", sum)

