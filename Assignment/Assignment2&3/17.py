n = 5
def oddseries(n):
    odd_sum = 0
    for i in range(1, n+1):
        odd_sum += ((2*i)**2) / (2*i-1)
    return odd_sum

def evenseries(n):
    even_sum = 0
    for i in range(1, n+1):
        even_sum += ((2*i)**2) / (2*i)
    return even_sum

# Example usage
n = 5
todd = oddseries(n)
teven = evenseries(n)

print("Sum of the odd series:",tesult)
print("Sum of the even series:", tresult)
 
