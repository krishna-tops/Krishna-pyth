#acording to input check the avability for discount and showing final invoice of amount payable with discount


Totalamount=0
Totalpaymentamount=0

Name=input("Enter name: ")
age=int(input("Enter age:"))
Totalamount=int(input("Enter total amount: "))

if age >= 18 and age <= 30 and Totalamount >= 5000:
    Discount = 20
elif age > 30 and age <= 50 and Totalamount >= 5000:
    Discount = 30
elif age > 50 and Totalamount >= 5000:
    Discount = 50
else:
    Discount = 0

Discountamount = Totalamount*Discount/100

Totalpayableamount=Totalamount-Discountamount

print("================INVOICE================")

print("Name : ",Name)
print("age : ",age)
print("Total amount : ",Totalamount)
print("Discount amount : ",Discountamount)
print("Total payable amount : ",Totalpayableamount)
