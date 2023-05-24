#first need to generate custome code of fibonaci series
def generate_fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
#with using while loop
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series
#then take an number int input from user 
n = int(input("Enter a number: "))
#lastly print the custom generated fibonacci series 
fibonacci_series = generate_fibonacci_series(n)
print("Fibonacci Series:",fibonacci_series)

