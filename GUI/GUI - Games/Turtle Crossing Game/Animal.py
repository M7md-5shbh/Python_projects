from turtle import Turtle

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(20)

    def at_end(self):
        if self.ycor() >= 260:
            return True
        else:
            return False

    def reset_position(self):
        self.goto(0, -280)

