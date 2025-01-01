def a_path_is_clear():
    if wall_in_front() and wall_on_right():
        return True
    else:
        return False

def turn_right():
    for i in range(3):
        turn_left()

def jump():
    while not front_is_clear():
        turn_left()
    while not right_is_clear() and front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()
    elif a_path_is_clear():
        jump()
    
