# importing the Screen object from the turtle module, for any errors, try to install it with pip install "turtle"
from turtle import Screen
import time
# make sure to download the rest of the files in this directory into the same directory as this one
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snack Game")

# screen.tracer turns off the turtle animation until the screen.update command is given
screen.tracer(0)

# creating objects of the classes we imported
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# binding the keyboard keys with functions for the snake's movement 
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with tail
    for body in snake.snake_body[2:]:
        if snake.head.distance(body) < 10:
            is_game_on = False
            scoreboard.game_over()
    screen.update()
    time.sleep(0.1)
    snake.move(20)




screen.exitonclick()
