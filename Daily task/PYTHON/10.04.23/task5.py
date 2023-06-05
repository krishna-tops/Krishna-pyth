import random

computer_guess = random.randint(1, 100)
number_chances = 5

print(" guess  number Game" )
for i in range(0,5):
    user_guess = int(input("Enter a number between 1 and 100: "))
    
    if user_guess == computer_guess:
        print("Congratulations! You guessed the number!")
        break
    
    elif user_guess < computer_guess:
        print("Hint: Think of a higher number.")
    else:
        print("Hint: Think of a lower number.")
    number_chances -= 1
    print(f"Chances left: ",number_chances)
    if num_chances == 0:
        print("GAME OVER !!!!!!!!!!!!")
