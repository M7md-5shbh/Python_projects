def a_path_is_clear():
    if wall_in_front() and wall_on_right():
        return True
    else:
        return False
    
def turn_right():
    for i in range(3):
        turn_left()
def go_right():
    turn_right()
    move()
    move()

go_right_count = 0
take()
turn_left()
move()
while not at_goal():
    if wall_in_front() and right_is_clear():
        go_right()
        go_right_count +=1
        if go_right_count > 2 and carries_object():
            put()
    elif a_path_is_clear():
        turn_left()
    elif front_is_clear():
        move()
