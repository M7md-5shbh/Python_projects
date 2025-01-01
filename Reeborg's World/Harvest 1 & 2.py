def turn_right():
    for i in range(3):
        turn_left()
move()
move()
turn_left()
move()

def harvest():
    field = 0
    while True:
        move()
        field += 1
        if field > 6:
                break
        while object_here():
            take()
        

for i in range(3):
    harvest()
    turn_right()
    move()
    turn_right()
    harvest()
    turn_left()
    move()
    turn_left()
