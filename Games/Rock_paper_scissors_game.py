# importing necessary modules
import random

# setting a global variable for the choices possible
choices = ['rock', 'paper', 'scissors']

# taking user input and generating a random choice for the computer
user_choice = int(input("Welcome to the Rock Paper Scissors Game! Choose one of the options: 0) rock 1) paper 2) scissors, press any other number to quit \n"))
computer_choice = random.choice(choices)
computer_choice = choices.index(computer_choice)

# defining the conditions for deciding who wins in a loop
while user_choice in [0, 1, 2]:
    print("your choice: ", choices[user_choice], "\ncomputer choice: ", choices[computer_choice])
    if user_choice == 0:
        if computer_choice == 0:
            print("it's a draw!")
        if computer_choice == 1:
            print("You lose!")
        if computer_choice == 2:
            print("You win!")

    if user_choice == 1:
        if computer_choice == 0:
            print("You win!")
        if computer_choice == 1:
            print("it's a draw!")
        if computer_choice == 2:
            print("You lose!")

    if user_choice == 2:
        if computer_choice == 0:
            print("You lose!")
        if computer_choice == 1:
            print("You win!")
        if computer_choice == 2:
            print("it's a draw!")

    user_choice = int(input("wanna continue the game? Choose one of the options: 0) rock 1) paper 2) scissors\npress any other number to quit \n"))

print("Thank you for playing!")
