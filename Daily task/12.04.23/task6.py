user_input = input("Enter a string: ")

capital_count = 0
small_count = 0

for i in user_input:
    if i.isupper():
        capital_count += 1
    elif i.islower():
        small_count += 1

print("Number of capital letters:", capital_count)
print("Number of small letters:", small_count)
