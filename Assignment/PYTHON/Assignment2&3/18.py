#first to  dfefine function using def
def factorial(numb):
    if numb == 0:
        return 1
    else:
        return numb * factorial(numb-1)
#take a input from user as an int
num = int(input("Enter a number: "))
#then check wheather entered number is negative or not
if num < 0:
    print("Factorial cannot be calculated for negative numbers.")
else:
    final = factorial(num)
    print("The factorial of", num, "is", final)
