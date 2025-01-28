from tkinter import *
import pandas as pd
from random import randint


# reading data from csv that's attached in this directory
df = pd.read_csv('esp-eng.csv', delimiter=',', header=None)
# turning the data into a zip object with each word and its meaning in a tuple
data = zip(df[0], df[1])
# turning it into a dictionary for easier processing of the data using dictionary comprehension
data = {i: v for i, v in enumerate(data)}

# creating two lists, each with the words of a language to use in the translate function
english_words = [data[key][1] for key in data.keys()]
spanish_words = [data[key][0] for key in data.keys()]

# random number to use to display a random word each time
index = randint(0, len(data)-1)


# ------------------- Spanish to English  ------------------- #
def spanish_to_english(reverse=False):
    """
    Displays the translation on the canvas from spanish words to english words. and vice-versa if reverse is True.
    :param reverse: bool
    :return: doesn't return anything
    """
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=data[index][1], fill='white')
    canvas.itemconfig(current_image, image=card_back)
    if reverse:
        canvas.itemconfig(language, text='Spanish', fill='black')
        canvas.itemconfig(word, text=data[index][0], fill='black')
        canvas.itemconfig(current_image, image=card_front)


# ------------------- New word ------------------- #
def new_word():
    """
    Generates a new word by changing the index variable and places it into the canvas using spanish_to_english() method.
    :return: None
    """
    global index
    index = randint(0, len(data) - 1)
    spanish_to_english(reverse=True)


# ------------------- Translate Function ------------------- #
def translate():
    """
    Performs the translation of spanish words to english words based on which language the word in the "word canvas object" belongs to.
    :return: None
    """
    global index
    if canvas.itemcget(word, "text") in spanish_words:
        spanish_to_english()
    elif canvas.itemcget(word, "text") in english_words:
        spanish_to_english(reverse=True)

# initializing the window, with a title, minimum size, background color and some padding
window = Tk()
window.title("Flash Card")
window.minsize(width=850, height=600)
window.configure(bg="#B1DDC6", padx=50, pady=50)

# creating the canvas images with the images that are attached in this directory
canvas = Canvas(window, width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
current_image = canvas.create_image(400, 263, image=card_front)

# creating the canvas texts
language = canvas.create_text(380, 150, text="Spanish", font=("Arial", 40, 'italic'))
word = canvas.create_text(380, 263, text=data[index][0], font=("Arial", 60, 'bold'))
# displaying using tkinter's geometry manager, grid
canvas.grid(column=0, row=0,columnspan=3, sticky=(N, S, W, E))

# creating and displaying the arrow and translate buttons
arrow_image = PhotoImage(file="./images/next.png")
arrow_button = Button(image=arrow_image, bg="#B1DDC6", highlightthickness=0,command=new_word)
arrow_button.grid(column=2, row=1)

translate_img = PhotoImage(file="./images/translate.png")
display_translation_button = Button(image=translate_img, command=translate, highlightthickness=0, bg="#B1DDC6")
display_translation_button.grid(column=1, row=1)

# to keep the program running until it is closed
window.mainloop()
