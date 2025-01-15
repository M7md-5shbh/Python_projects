from turtle import Turtle
align = "center"
font = ("Courier", 80, "normal")

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.hideturtle()
            self.penup()
            self.pencolor("black")
            self.score = 0


        def draw_lines(self, position):
            self.goto(position)
            self.setheading(90)
            while self.position()[1] < -(position[1]):
                self.pendown()
                self.forward(100)
                self.penup()
                self.forward(50)
            self.pendown()
            for i in range(5):
                self.setheading(360 - i * 90) # 360 270 180 90
                self.forward(100)
                while (self.position()[0] > -390 and self.position()[0] < 390) or (self.position()[1] > -290 and self.position()[1] < 290):
                    self.forward(100)

        def write_score(self, position, score=None):
            self.goto(position)
            self.write(arg=f"{self.score}", align=align, font=font)


        def increase_score(self, position):
            self.clear()
            self.score += 1
            self.write_score(position, self.score)


