# written by M7md-5shbh
# Number Guessing Game
#--------------------------------------------

# importing the necessary module for pseudo-randomization
import random
art = r"""
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
"""

# defining the logic function of the game 
def guess_the_number():
    """
    A function that plays the Guess The Number Guessing Game
    :return: None
    """
    # declaring important variables for the game
    lives = 0
    num_to_guess = random.randint(0,100)
    # Keeping track of guesses made and displaying them later to the player
    guesses_made = {}
    # choosing difficulty level to allow for more lives depending on the level
    game_difficulty = input("Choose the difficulty level of your game: acceptable answers are: easy or hard\n").lower()
    if game_difficulty == "easy":
        lives = 10
        print(f"You have {lives} lives. Go for it!")
    elif game_difficulty == "hard":
        lives = 5
        print(f"You have {lives} lives. Go for it!")
    while lives > 0:
        high_or_low = ""
        player_guess = input("Try to guess a whole number between 0 and 100: \n")
        if player_guess.isnumeric():
            player_guess = int(player_guess)
        else:
            print("You entered an invalid input that's not a whole number, do it correctly next time ;) ")
            print("Goodbye!")
            break
        if player_guess == num_to_guess:
            print("You guessed the right number! you won!")
            break
        elif player_guess > num_to_guess:
            print("too high!!")
            high_or_low = "high"
        elif player_guess < num_to_guess:
            print("too low!!")
            high_or_low = "low"
        guesses_made[player_guess] = high_or_low
        lives -= 1
        print(f"You have {lives} lives left!")
        print(f"Guesses made: {guesses_made}")
    else:
        print("You did not choose the difficulty level correctly or ran out of lives :( , feel free to take another go at it!")

while True:
    go_again = input("Would you like to play Guess The Number game? type 'y' to continue or anything else to quit: \n")
    if go_again.lower() == 'y':
        print(art)
        guess_the_number()
    else:
        break
