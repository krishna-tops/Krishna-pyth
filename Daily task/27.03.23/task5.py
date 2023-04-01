n1=int(input("sub1 :"))
n2=int(input("sub2 :"))
n3=int(input("sub3 :"))
n4=int(input("sub4 :"))
n5=int(input("sub5 :"))
total=n1+n2+n3+n4+n5
per=total/5
print("Percentage",per)
if per>=85 :
    print("Grade:A")
elif per>=75 :
    print("Grade:B")
elif per>=45 :
    print("Grade:C")
else :
    print("Fail")


