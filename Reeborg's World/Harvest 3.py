def turn_right():
    for i in range(3):
        turn_left()move()
move()
turn_left()
move()

def harvest():
    field = 0
    while True:
        move()
        while object_here():
            take()
        if not object_here():
            if field >= 6:
                break
            put()
            field += 1

for i in range(3):
    harvest()
    turn_right()
    move()
    turn_right()
    harvest()
    turn_left()
    move()
    turn_left()
