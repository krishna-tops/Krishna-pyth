#take ainput as a string from user
str = str(input("Enter the string : "))
#make a condition of string lenth
if len(str)<3:
    print(str)
else:
    if str.endswith("ing"):
        print(str + "ly")
    else:
        print(str + "ing")
        

