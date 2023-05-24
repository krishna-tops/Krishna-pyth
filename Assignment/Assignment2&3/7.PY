#first to take two numbers from user
n1 = int(input("Enter a number1 :"))
n2 = int(input("Enter a number2 :"))

#then aplly loop to find both numbers GCD
for i in range(1,n2+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        
print("GCD for",n1, "and" ,n2,"is :" ,gcd)
