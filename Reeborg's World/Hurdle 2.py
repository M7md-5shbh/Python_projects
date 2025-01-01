def turn_right():
    for i in range(3):
        turn_left()

def jump():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

move()
jump()
for i in range(5):
    if at_goal():
        break
    turn_left()
    move()
    jump()
    
        
