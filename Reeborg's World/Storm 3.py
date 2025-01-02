# There multiple ways to do this puzzle, a couple of ways to go about it are going up and down or side by side until you cover all lines
# solution 1: going up and down (easier)
think(0)
def turn_around():
    repeat 2:
        turn_left()
def turn_right():
    repeat 3:
        turn_left()
        
def toss_the_leaves():
    turn_around()
    while front_is_clear():
        move()
    if at_goal():
        turn_right()
        while carries_object():
            toss()
        else:
            done()
            
def go_around():
    turn_right()
    move()
    move()
    turn_right()
    move()
    turn_left()
def go_to_the_yard():   
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_right()
    while front_is_clear():
        if object_here():
            take()
        else:
            move()
    else:
        while object_here():
            take()
        else:
            turn_right()
            move()
            turn_right()

go_to_the_yard()
while True:
    if not front_is_clear():
        if is_facing_north():
            while object_here():
                take()
            else:
                turn_right()
                if wall_in_front():
                    turn_right()
                    while front_is_clear():
                        move()
                    else:
                        turn_left()
                        toss_the_leaves()              
                move()
                turn_left()
                if front_is_clear():
                    repeat 2:
                        move()
                    turn_left()
                    move()
                    turn_right()
                else:        
                    turn_around()
        else:
            while object_here():
                take()
            else:
                turn_left()
                if wall_in_front():
                    toss_the_leaves()
                else:
                    move()
                    if right_is_clear():
                        turn_right()
                        move()
                        move()
                        turn_right()
                        move()
                        turn_left()
                    else:
                        turn_left()
    elif object_here():
        take()
    else:
        move()
""" 
================================================================================================================================================================================================================
================================================================================================================================================================================================================

"""
# solution 2: going side by side (harder because you need to account for row and column numbers, steps taken, etc)
think(0)
def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left()
def take_all():
    while object_here():
        take()
def move_a_row_left():
    if not front_is_clear():
        turn_right()
        move()
        repeat 2:
            turn_left()
            move()
            move()
        turn_left()
        move()
        turn_right()
        return True
    move()
    turn_left()
    
def move_a_row_right():
    if not front_is_clear():
        turn_left()
        move()
        repeat 2:
            turn_right()
            move()
            move()
        turn_right()
        move()
        turn_left()
        return True
    move()
    turn_right()

def toss_all():
    while carries_object():
        toss()

move()
steps = 1
columns_count = 2 # accounting for first_column we're at and last one
rows_count = 1 # starting row count
num_of_walls = 0 # number of walls, to add a condition helping the robot notice that it's at the compost  bin
row_number = 1 # row_number the robot is at while moving
compost_bin = True 

while not at_goal():
    if front_is_clear():
        take_all()
        
        if columns_count - steps == 2:
            if (rows_count - row_number == 1 or rows_count - row_number == 0) and num_of_walls > 1:
                take_all()
                turn_left()
                while True:
                    try:
                        if not front_is_clear():
                            turn_right()
                            move()
                            turn_left()
                            move()
                            row_number -= 1
                        else:
                            move()
                        row_number -= 1
                    except:
                        turn_around()
                        row_number +=2
                    if row_number == 2:
                        turn_right()
                        while not wall_in_front():
                            move()
                        toss_all()
                        break
                turn_left()
                move()
                turn_right()
                move()
                done()
            elif compost_bin:
                take_all()
                turn_left()
                if move_a_row_left():
                    row_number += 1
                    steps = 1
                else: 
                    row_number += 1
                    steps = 0
                compost_bin = False
            elif row_number % 2 == 0:
                take_all()
                turn_left()
                if move_a_row_left():
                    row_number += 1
                    steps = 1
                else: 
                    row_number += 1
                    steps = 0
                take_all()

            elif row_number % 2 == 1:
                take_all()
                turn_right()
                if move_a_row_right():
                    row_number += 1
                    steps = 1
                else: 
                    row_number += 1
                    steps = 0
                take_all()
        
        else:
            move()
        steps += 1
            
        
        
        if row_number == 1 and num_of_walls == 0:
            columns_count +=1
        if num_of_walls == 1:
            rows_count += 1
        

        
                
    elif not front_is_clear():
        if wall_on_right():
            turn_left()
            num_of_walls += 1
            if num_of_walls > 3:
                take_all()
                move()
                take_all()
                turn_right()
                move()
                turn_left()
                steps = 1
                row_number += 1
        if wall_in_front():
            if row_number % 2 == 0:
                turn_left()
                move()
                turn_left()
                move()
                row_number += 1
                steps = 1
            elif row_number % 2 == 1:
                turn_right()
                move()
                turn_right()
                move()
                row_number += 1
                steps = 1
            
        if columns_count - steps > 2:
            if not front_is_clear():
                turn_right()
                take_all()
                move()
                turn_left()
                move()
                move()
                turn_left()
                move()
                turn_right()
                take_all()
                steps += 2
               
                    
                        
                    
                if columns_count - steps == 1:
                    if row_number % 2 == 0:
                        turn_left()
                        move()
                        turn_left()
                        row_number += 1
                        steps = 0
                    elif row_number % 2 == 1:
                        take_all()
                        turn_right()
                        move()
                        turn_right()
                        row_number += 1
                        steps = 0
