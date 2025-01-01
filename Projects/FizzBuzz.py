# This game expands a bit on the FizzBuzz game, checking to make sure the input is numeric and if the number isn't divisible by either 3 or 5

print("Welcome to FizzBuzz Game")
user_input = input("Enter a number: \n")

while user_input.isnumeric(): # checks to see if the input string is a numeric string before changing its type to int
    user_input = int(user_input)
    if user_input % 3 != 0 and user_input % 5 != 0 :
        print("number isn't divisible by 3 or 5, try a different one!")
    elif user_input % 3 == 0 and user_input % 5 == 0:
        print("FizzBuzz")
    elif user_input % 3 == 0:
        print("Fizz")
    elif user_input % 5 == 0:
        print("Buzz")

    user_input = input("Enter another number: \n")

else:
    print("You didn't input a valid number!")
    print("valid numbers include whole numbers!!! Run again and do it right next time ;p")
