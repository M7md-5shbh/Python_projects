def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

while not at_goal():
    move()
turn_right()
move()

previous_wall = False
next_wall = False

while not at_goal():
    if front_is_clear(): 
        if wall_on_right():
            move()
            previous_wall = True
        elif not wall_on_right():
            move()
            if previous_wall and wall_on_right():
                turn_around()
                move()
                turn_left()
                build_wall()
                previous_wall = False
                turn_left()
            if not wall_on_right():
                turn_around()
                move()
                turn_left()
                move()
    if wall_in_front():
        turn_left()
    
