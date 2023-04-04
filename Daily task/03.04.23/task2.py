n=8
for i in range(0,6):
    for j in range(0,n):
        print(end=" ")
    n=n-2
    for j in range(0,i+1):
        print("*",end=" ")
    print()

