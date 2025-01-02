def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left()
def take_all():
    # defining a function to take all objects in one spot instead of just one
    while object_here():
        take()
    
# moving out of the goal space        
move()

# defining global variables | second_row is defined to use it as a condition since it is the only row that differs from the rest
row_number = 1
second_row = True

while not at_goal():
    if front_is_clear():
            take_all()
            move()
    elif row_number >= 6: # if we reached the last row
        turn_left()
        while not wall_in_front(): # moving towards the bin
            move()
        while carries_object(): # tossing all objects carried at the bin
            toss()
        turn_left()
        move()
        turn_right()
        move()
        move()
        turn_right()
        move()
    elif wall_in_front(): 
        # using row numbers to decide whether to go left or right, if the number is odd, we go left, and if even we go right, except at row number 2
        if (row_number % 2 == 1): # if odd
            turn_left()
            take_all()
            move()
            turn_left()
            row_number +=1
        elif second_row:
            turn_right()
            take_all()
            move()
            turn_left()
            take_all()
            move()
            turn_around()
            second_row = False # switching it to False so this condition won't trigger again
            row_number += 1
        elif (row_number % 2 == 0): # if even
            turn_right()
            take_all()
            move()
            turn_right()
            row_number +=1
