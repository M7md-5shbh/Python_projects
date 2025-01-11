from turtle import Turtle

# setting global variables for the alignment and font used in the scoreboard
align = "center"
font = ("Courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        position_x, position_y = -30, 250
        self.goto(position_x, position_y)
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=align, font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=align, font=font)
