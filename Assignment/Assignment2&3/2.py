string = input("Enter a string: ")
substring = input("Enter a substring: ")

count = string.count(substring)

print("The substring '{}' appears {} times in the string '{}'".format(substring, count, string))
