#first to take an string
str1 = ("I am not poor ")
#then find the word not and poor
not_find = str1.find("not")
poor_find = str1.find("poor")
#make acondition to replace it with good
if not_find>0 and poor_find>0:
    new1 = str1.replace("not", "good").replace("poor", "good ")
    print(" ",new1)
else:
    print(" ",str1)
