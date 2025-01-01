def turn_right():
    for i in range(3):
        turn_left()

def a_path_is_clear():
    if wall_in_front() and wall_on_right():
        return True
    else:
        return False


def jump():
    while not front_is_clear() and a_path_is_clear():
        turn_left()
    move()
    if wall_in_front() or wall_on_right():
        return
    turn_right()
    move()
    turn_right()
    move()



while not at_goal():
    if front_is_clear() and not is_facing_north():
        move()
    elif is_facing_north():
        turn_right()
    
    elif (wall_in_front() and wall_on_right() 
          and not right_is_clear() and not front_is_clear()):
        jump()
