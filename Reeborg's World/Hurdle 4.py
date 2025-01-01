def a_path_is_clear():
    if wall_in_front() and wall_on_right():
        return True
    else:
        return False

def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif (not front_is_clear() and not right_is_clear()
    and a_path_is_clear()):
        turn_left()
    elif (not front_is_clear() and right_is_clear()):
        turn_right()
        move()
          
