# make sure to download the US_Game_Mechanic, the gif file, and data file
# to the same directory along with this file for the game to work

# importing necessary modules for the game
import turtle
import sys
from US_Game_Mechanic import Game_Mechanics

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_already_answered = []

# creating instances of the Game_Mechanics class to help draw on the screen using more than one turtle
mechanics = Game_Mechanics()
correct_answers = Game_Mechanics()

states = mechanics.data.state.to_list()

while True:
    answer_state = screen.textinput(title=f"{len(states_already_answered)}/{len(mechanics.data)} Guess State Name", prompt="Enter State Name (Enter Q to quit)").title()
    if answer_state == "Q":
        print(f"You got {len(states_already_answered)} answers correct out of 50")
        print("Thank you for playing!")
        sys.exit()
        break
    if answer_state in states_already_answered:
        mechanics.repeated_answer(answer_state)
        continue
    if answer_state in states:
        correct_answers.correct(answer_state)
        states_already_answered.append(answer_state)
    else:
        mechanics.does_not_exist(answer_state)

    if len(states_already_answered) == len(mechanics.data["state"]):
        mechanics.win()
        break


screen.mainloop()