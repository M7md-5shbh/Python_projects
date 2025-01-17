# importing the necessary modules
# turtle usually comes preinstalled but if it shows a "module not found" error, install it with
# pip install turtle or python -m pip install turtle
from turtle import Turtle, Screen

# creating a turtle and screen instances to use
t = Turtle()
screen = Screen()

# defining functions that will be used to decide which way the turtle goes and to clear the screen
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_clockwise():
    t.right(10)

def move_counterclockwise():
    t.left(10)

def clear_screen():
    t.clear()
    t.up()
    t.home()
    t.down()

# The screen.listen Sets the focus on TurtleScreen (in order to collect key-events) 
screen.listen()

# The screen.onkey method binds a key to a function when pressed
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="c", fun=clear_screen)

# screen.mainloop helps not let the screen close right after the commands execute but rather wait for you
# to exit from it or you could use t.exitonclick() instead to make the screen exit when you click on the screen
screen.mainloop()
