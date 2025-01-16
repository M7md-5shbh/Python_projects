from turtle import Turtle
# the starting position list is used to create the body of the snake at different places
starting_positions = [(0,0), (-20, 0), (-40, 0)]
class Snake(Turtle):
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in starting_positions:
            self.add_body(position)
        self.head = self.snake_body[0]

    def add_body(self, position):
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.snake_body.append(square)

    def extend(self):
        self.add_body(self.snake_body[-1].pos())


    def move(self, move_distance):
        for square in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[square].goto(self.snake_body[square - 1].pos())
        self.head.forward(move_distance)

    # Movement functions to bind with the keyboard keys
    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)
