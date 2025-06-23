# Rock Paper Scissors Game

import random

options = ["Rock", "Paper", "Scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input < 0 or user_input > 2:
    print("Invalid input. You lose!")
else:
    print(f"You chose: {options[user_input]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {options[computer_choice]}")

    if user_input == computer_choice:
        print("It's a draw!")
    elif (user_input - computer_choice) % 3 == 1:
        print("You win! 🎉")
    else:
        print("You lose 😢")
