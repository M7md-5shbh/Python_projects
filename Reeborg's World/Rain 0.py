for i in range(6):
    move()

build_wall()
turn_left()
turn_left()
while not at_goal():
    move()
