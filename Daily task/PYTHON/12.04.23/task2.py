name=str(input("Enter something :"))
vowels_count=0
consonant_count=0
white_space=0
for i in name:
    if i==" ":
        white_space+=1
    elif i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vowels_count+=1
    else:
        consonant_count+=1
    
    
print("vowels_count =",vowels_count)
print("consonant_count =",consonant_count)
print("white_count =",white_space)
