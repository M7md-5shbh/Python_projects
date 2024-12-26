# written by M7md-5shbh
# Date: 2024-12-26
# a code that returns the highest occuring letter in a given text/sentence
#--------------------------------------------

# Simple way
def highest_occuring_letter(sentence):
    """
        Finds the highest occurring letter in the given sentence, ignoring spaces.

        This function iterates through each character in the sentence, counts the occurrences
        of each letter, and identifies the letter with the highest frequency.

        Parameters:
        sentence (str): The input sentence from which to find the highest occurring letter.

        Returns:
        tuple: A tuple containing the letter (str) with the highest frequency and its count (int).
    """
    letter = ""
    count  = 0
    for char in sentence:
        if char == " ":
            continue
        elif sentence.count(char) > count:
            letter = char
            count = sentence.count(char)
        else:
            continue

    return letter, count


sentence = "The quick brown fox jumps over the lazy dog."

print(highest_occuring_letter(sentence))


# another way using a lambda function
# it is better to always use import only at the start of your python code, but this is for demonstration purposes
import string

def highest_occuring_letter(sentence):
    """
    Removes unnecessary punctuation and whitespace from the given sentence,
    then transforms each letter and its frequency into a dictionary.
    Finally, it sorts the dictionary based on frequency using a lambda function.

    Parameters:
    sentence (str): The input sentence from which to count letter frequencies.

    Returns:
    tuple: A tuple containing the letter (str) and its frequency (int).
    """
    illegal_chars = string.punctuation + string.whitespace
    char_freq = {}
    for char in sentence:
        if char in illegal_chars:
            continue
        elif char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    char_freq_sorted = sorted(char_freq.items(), key = lambda kv: kv[1], reverse=True)
    return char_freq_sorted[0]

print(highest_occuring_letter(sentence))



