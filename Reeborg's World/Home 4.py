def turn_right():
    for i in range(3):
        turn_left()

for i in range(50):
    if front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        if at_goal():
            break
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
    
