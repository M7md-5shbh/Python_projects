from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("slowest")
        self.move_x = 10
        self.move_y = 10



    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
       

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()

