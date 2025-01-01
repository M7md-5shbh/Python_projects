# importing necessary modules
import random
import string

# defining the variable to save the generated password in
pw = ""

print("Welcome to the Password Generator!")
# taking user specifications for the password
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))
num_of_digits = int(input("How many numbers would you like in your password?\n"))

# taking random values from the string module based on the user specifications, the sample function returns a list
rand_values = random.sample(string.ascii_letters, num_of_letters) + random.sample(string.punctuation, num_of_symbols) + random.sample(string.digits, num_of_digits)

# shuffling the random values list
random.shuffle(rand_values)

# iterating over the values in the list to add them to our pw variable
for value in rand_values:
    pw += value

print(f"The generated password is: {pw}")
