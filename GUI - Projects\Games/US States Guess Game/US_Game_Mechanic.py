from turtle import Turtle
import pandas as pd
import time

data = pd.read_csv("50_states.csv")
align = "center"
arial_font = ("Arial", 20, "bold")
class Game_Mechanics(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.data = data

    def win(self):
        self.goto(0, 300)
        self.write(arg="YOU WIN!", align=align, font=arial_font)


    def correct(self, answer):
        state_details = data[self.data.state == answer]
        self.goto(state_details.x.item(), state_details.y.item())
        self.write(answer, align=align, font=("Arial", 10, "bold"))

    def repeated_answer(self, answer):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"You already answered: '{answer}'", align=align, font=arial_font)
        time.sleep(2)
        self.clear()

    def does_not_exist(self, answer):
        self.goto(0, 270)
        self.write(arg=f"State {answer} Does not exist", align=align, font=arial_font)
        time.sleep(2)
        self.clear()