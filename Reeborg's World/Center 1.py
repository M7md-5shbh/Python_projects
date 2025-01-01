# counting the steps taken
steps = 1

while front_is_clear():
    move()
    steps +=1

turn_left()
turn_left()

# dividing the steps by half, used // because it returns the floor() of a number and doesn't turn it into a floating point number
return_steps = steps // 2

for i in range(return_steps):
    move()
put()
