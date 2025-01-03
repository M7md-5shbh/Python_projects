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
    
# in the code above, I used a range higher than the actual size and informed it to stop when it reaches a goal at a corner with walls in front and right
# to make it simpler, I wrote another code to do the same job, with a function called L_turn as the path is made of L-shaped paths running the same function 4 times to reach the goal

def turn_right():
    for i in range(3):
        turn_left()

def L_turn():
    while True:
        if front_is_clear():
            move()
        elif not front_is_clear():
            if not right_is_clear():
                if at_goal():
                    done()
                turn_left()
            else:
                turn_right()
                move()
                turn_right()
                break
for i in range(4):
    L_turn()
