# importing modules
import string

# defining the function for our code
def ceaser(original_text, shift_by, encode_or_decode):
    output_text = ''
    if encode_or_decode == "decode":
        shift_by *= -1
    for char in original_text.lower():
        if char not in string.ascii_lowercase:
            output_text += char
        else:
            shifted_position = (string.ascii_lowercase.index(char) +  shift_by) % 26
            output_text += string.ascii_lowercase[shifted_position]
    return f"Here's the {encode_or_decode}d result: {output_text}"


keep_going = True

while keep_going:
    operation = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    message = input("Type your message: \n")
    shift = int(input("Type the shift value: \n"))

    print(ceaser(original_text=message, shift_by=shift, encode_or_decode=operation))

    restart = input("Type 'yes' if you want to go again, otherwise type 'no': \n").lower()
    if restart == "no":
        keep_going = False
        print("Goodbye!")
