# written by M7md-5shbh
# Rock paper scissors game
#--------------------------------------------
# importing necessary modules
import random

# setting a global variable for the choices possible
choices = ['rock', 'paper', 'scissors']

# taking user input and generating a random choice for the computer
user_choice = int(input("Welcome to the Rock Paper Scissors Game! Choose one of the options: 0) rock 1) paper 2) scissors, press any other number to quit \n"))
computer_choice = random.choice(choices)
computer_choice = choices.index(computer_choice)

# defining the logic behind the game
while user_choice in [0, 1, 2]:
    print("your choice: ", choices[user_choice], "\ncomputer choice: ", choices[computer_choice])
    if 0 < user_choice <= 3:
        print("You typed an invalid choice. Please try again.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    user_choice = int(input("wanna continue the game? Choose one of the options: 0) rock 1) paper 2) scissors\npress any other number to quit \n"))

print("Thank you for playing!")
