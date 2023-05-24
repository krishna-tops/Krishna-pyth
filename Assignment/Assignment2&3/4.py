#program to combine two string
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
string = str1+" "+str2
string = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
print("Combined string :",string)
