# defining global variables
walls = 0
horizontal_steps = 1
vertical_steps = 1

# counting horizontal steps taken
while front_is_clear():
    move()
    horizontal_steps +=1

# counting number of walls the robot observed in front and on left, to check if the path is only on the x axis
while not front_is_clear():
    walls += 1
    turn_left()

while front_is_clear():        
    # if walls > 1, then the path is only on the x axis, so no need to measure for vertical steps
    if walls > 1:
        break
    move()
    vertical_steps +=1
else:
    turn_left()
 
half_hor_steps = horizontal_steps // 2
half_ver_steps = vertical_steps // 2

if not front_is_clear():
    turn_left()
for x in range(half_hor_steps):
    if wall_in_front():
        break
    move()
if not front_is_clear():
    turn_left()
for y in range(half_ver_steps):
    if wall_in_front():
        break
    move()
put()
