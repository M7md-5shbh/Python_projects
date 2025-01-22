import turtle
from turtle import Turtle
import random

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'brown', 'black']
y = [i*20 for i in range(13)] + [i*-20 for i in range(1, 13)]

class Car(Turtle):
    car_speed = 10
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(colors))
        coordinates = (390, random.choice(y))
        self.goto(coordinates)


    def move(self):
        if -390 <= self.xcor() <= 390:
            self.goto(self.xcor() - Car.car_speed, self.ycor())
        else:
            self.hideturtle()
            for t in turtle.turtles():
                if not t.isvisible():
                    del t

