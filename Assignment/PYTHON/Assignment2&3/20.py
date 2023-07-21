import random

# to create a strong password with uppercase letter, lowercase Letter, number and special characters
def generateStrongPassword():
    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charsLow = "abcdefghijklmnopqrstuvwxyz"
    charsNumber = "0123456789"
    charsSpecial = "!@#$%&*()[]{}"
    password = ''
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    return password



print('Generating password 1',generateStrongPassword())



