def turn_right():
    for i in range(3):
        turn_left()

move()
turn_right()
move()
while not at_goal():
    if wall_in_front():
        turn_left()
    elif front_is_clear():
        if wall_on_right():
            move()
        else:
            turn_right()
            build_wall()
            turn_left()
     
