# written by M7md-5shbh
# Hangman Game
#--------------------------------------------

import random

common_verbs = ["had", "were", "can", "said", "use", "do", "will", "would", "make", "like", "has", "look", "write", "go", "see", "could", "been", "call", "am", "find", "did", "get", "come", "made", "may", "take", "know", "live", "give", "think", "say", "help", "tell", "follow", "came", "want", "show", "set", "put", "does", "must", "ask", "went", "read", "need", "move", "try", "change", "play", "spell", "found", "study", "learn", "should", "add", "keep", "start", "thought", "saw", "turn", "might", "close", "seem", "open", "begin", "got", "run", "walk", "began", "grow", "took", "carry", "hear", "stop", "miss", "eat", "watch", "let", "cut", "talk", "being", "leave"]

common_nouns = ["word", "time", "number", "way", "people","water", "day", "part", "sound", "work","place", "year", "back", "thing", "name","sentence", "man", "line", "boy", "farm","end", "men", "land", "home", "hand","picture", "air", "animal", "house", "page","letter", "point", "mother", "answer", "America","world", "food", "country", "plant", "school","father", "tree", "city", "earth", "eye","head", "story", "example", "life", "paper","group", "children", "side", "feet", "car","mile", "night", "sea", "river", "state","book", "idea", "face", "Indian", "girl","mountain", "list", "song", "family"]

common_adjectives = ["each", "other", "many", "some", "two","more", "long", "new", "little", "most","good", "great", "right", "mean", "old","any", "same", "three", "small", "another","large", "big", "even", "such", "different","kind", "still", "high", "every", "own","light", "left", "few", "next", "hard","both", "important", "white", "four", "second","enough", "above", "young"]

common_adverbs = ["not", "when", "there", "how", "up","out", "then", "so", "no", "first","now", "only", "very", "just", "where","much", "before", "too", "also", "around","well", "here", "why", "again", "off","away", "near", "below", "last", "never","always", "together", "often", "once", "later","far", "really", "almost", "sometimes", "soon"]

all_words = common_verbs + common_nouns + common_adjectives + common_adverbs
word_to_guess = random.choice(all_words)

underscored_word = len(word_to_guess) * "_"
initial_underscored_word = underscored_word
underscored_word_list = list(underscored_word)
progress_lives = 6
print("Welcome to the hangman game, try to guess the letters")
if word_to_guess in common_adjectives:
    print("the word is an adjective")
elif word_to_guess in common_adverbs:
    print("the word is  adverb")
elif word_to_guess in common_nouns:
    print("the word is a noun")
elif word_to_guess in common_verbs:
    print("the word is a verb")
user_input = input(f"it is a {len(underscored_word)} letter word, you have 6 lives at the start, you lose one for each incorrect guess, so go ahead, try to guess a letter: \n")


def is_letter_in_word(letter, word):
    global progress_lives, underscored_word, underscored_word_list, initial_underscored_word
    for index,value in enumerate(word):
        if word[index] == letter:
            underscored_word_list[index] = value
            continue
    underscored_word = "".join(underscored_word_list)
    if initial_underscored_word == underscored_word:
        print(f"{letter} is not in the word")
        progress_lives -= 1
        print(f"You have {progress_lives} lives left")
    else:
        initial_underscored_word = underscored_word
        #print(underscored_word)
    print(underscored_word)
    
    
is_letter_in_word(user_input, word_to_guess)

while (progress_lives > 0) and ("_" in underscored_word):
        user_guess = input("Try to guess another letter: ")
        is_letter_in_word(user_guess, word_to_guess)




if progress_lives == 0:
    print(f"the word was {word_to_guess}, you lost")
elif "_" not in underscored_word:
    print("congrats! YOU WON!")
