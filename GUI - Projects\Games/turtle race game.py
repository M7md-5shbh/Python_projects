# written by M7md-5shbh
# Turtle race game
#--------------------------------------------

# Importing the necessary modules 
# if any of them shows a module not found error, install it with pip install "module name"
import random
from turtle import Turtle, Screen

screen = Screen()

# setting up the screen size for the race
screen.setup(width=600, height=400)

# defining a function to create the turtles as customizable as possible all at once when needed
def turtle_maker(name, shape=None, color=None, penup=False):
    """
    :param name: Turtle name
    :param shape: (optional) shape of the turtle e.x. "arrow", "turtle", "circle", "square", "triangle", "classic"
    :param color: (optional) str or rgb tuple: color of the turtle
    :param penup: (optional) boolean if you want the penup
    :return: Turtle object
    """
    if shape is None:
        name = Turtle()
    else:
        name = Turtle(shape=shape)
    if type(color) == tuple:
        name.colormode(255)
    if color is None:
        pass
    else:
        name.color(color)
    if penup:
        name.up()
    else:
        pass
    return name

# setting the colors variable for the colors that will be used, but feel free to change them or add rgb color tuples
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# defining the logic for the race
def turtle_race():
    screen.clear()
    is_race_on = False
    # Taking the user input as a bet to see if he chooses the one that finished first
    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which turtle will win the race? Enter a color: red, orange, yellow, green, blue, purple")
    if user_bet:
        is_race_on = True

    turtles_list = []

    for i in range(6):
        turtle_name = "t" + str(i)
        # the program is designed to work with the shape turtle, but if you change it, make sure to change the finish line coordinates based on the size of the shape you choose
        turtle_name = turtle_maker(turtle_name, shape="turtle", color=colors[i], penup=True)
        turtles_list.append(turtle_name)
        # starting coordinates for each turtle
        turtle_name.goto(x=-280, y=-(100 - 30 * i))
    
    while is_race_on:
        for turtle in turtles_list:
            if turtle.xcor() > 270:
                is_race_on = False
                winning_color = turtle.color()[0]
                return winning_color, user_bet
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)


game_result, user_bet = turtle_race()

while True:
    if game_result == user_bet:
        play_again =screen.textinput(title="Results!",
                                     prompt=f"You Win! the {game_result} turtle won the race! want to play again? type yes/y or no/n")
    else:
        play_again = screen.textinput(title="Results!",
                                      prompt=f"You lose! the {game_result} turtle won the race! want to play again? type yes/y or no/n")
    if play_again.lower() in ["y", "yes"]:
        game_result, user_bet = turtle_race()
    else:
        break
screen.exitonclick()
