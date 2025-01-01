def turn_right():
    for i in range(3):
        turn_left()

while not wall_in_front():
    move()
    while object_here():
        take()

else:
    turn_left()
    move()
    turn_left()
while not wall_in_front():
    move()
while carries_object():
    toss()
    
turn_left()
move()
turn_right()
move()
