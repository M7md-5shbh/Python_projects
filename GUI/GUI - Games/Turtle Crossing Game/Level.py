from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.level = 1

    def write_level(self):
        self.clear()
        self.goto(-350, 260)
        self.write(arg=f"Level {self.level}", align="center", font=("Arial", 20, "bold"))

    def write_start_end(self):
        self.goto(-350, 250)
        self.pendown()
        while self.xcor() < 350:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 20, "bold"))