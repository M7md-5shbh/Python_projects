# importing the Screen object from the turtle module, for any errors, try to install it with pip install "turtle"
from turtle import Screen
import time
# make sure to download the rest of the files in this directory into the same directory as this one
from Paddle import Paddle
from Scoreboard import Scoreboard
from Ball import Ball

# defining the screen object and its setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("orange")
screen.title("Pong Game")
screen.tracer(0)

# creating paddle instances
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# drawing game lines where the ball is allowed to be at
line = Scoreboard()
line.draw_lines((0, -300))

# drawing scores above to keep track of scores
score_left = Scoreboard()
score_left.write_score((-180, 275))
score_right = Scoreboard()
score_right.write_score((180, 275))

# defining a ball instance 
ball = Ball()

# telling the screen to listen for keys pressed by the user based on what is defined after
screen.listen()
# left paddle controls
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
# right paddle controls
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)



is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if 280 < ball.ycor()  or ball.ycor() < -280 :
        ball.bounce_y()

    # detect collision with a paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball is out of bounds
    # right paddle
    if ball.xcor() > 380:
        score_left.increase_score((-180, 270))
        ball.reset_ball()

    # left paddle
    if ball.xcor() < -380:
        score_right.increase_score((180, 270))
        ball.reset_ball()

screen.mainloop()
