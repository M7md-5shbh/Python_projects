# importing necessary modules, if any module throws an error, try pip install "module name"
from turtle import Screen
import time
import random
# the modules after this should be downloaded along to the same directory for the game to work
from Animal import Animal
from Car import Car
from Level import Level

# defining the screen object and setting it up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)

# defining objects for the animal and level
animal = Animal()
level = Level()
level.write_level()
finish_line = Level()
finish_line.write_start_end()

# a list to holds the car objects created
cars = []

screen.listen()
screen.onkeypress(key="Up", fun=animal.move)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    if animal.at_end():
        animal.reset_position()
        Car.car_speed += 2
        level.level += 1
        level.write_level()

    if level.level <=3:
        random_chance = random.randint(1, 6)
    else:
        random_chance = random.randint(1, 4)
    if random_chance == 1:
        car = Car()
        cars.append(car)

    for car in cars:
        if car.distance(animal) < 20:
            level.game_over()
            is_game_on = False

        car.move()
    

screen.exitonclick()