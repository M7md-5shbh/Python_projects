# written by M7md-5shbh
# Higher-lower game using data scrapped from wikipedia
#--------------------------------------------
# importing necessary modules
# if you don't have any of the modules, you can download it from the terminal/cmd using 
# pip install "module name"
# or 
# python -m pip install "module name"
import random
import bs4
import requests
import re
import string
import json

# defining the initial data to work with
data = {
    1: {'name': 'Leonardo DiCaprio',
        'country': 'USA'},
    2: {'name': 'Ariana Grande',
        'country': 'USA'},
    3: {'name': 'Tom Hanks',
        'country': 'USA'},
    4: {'name': 'Rihanna',
        'country': 'Barbados'},
    5: {'name': 'Jeff Bezos',
        'country': 'USA'},
    6: {'name': 'Selena Gomez',
        'country': 'USA'},
    7: {'name': 'Kylie Jenner',
        'country': 'USA'},
    8: {'name': 'Dwayne \'The Rock\' Johnson',
        'country': 'USA'},
    9: {'name': 'Taylor Swift',
        'country': 'USA'},
    10: {'name': 'Kendall Jenner',
        'country': 'USA'},
    11: {'name': 'Kim Kardashian',
        'country': 'USA'},
    12: {'name': 'Will Smith',
        'country': 'USA'},
    13: {'name': 'Beyoncé',
        'country': 'USA'},
    14: {'name': 'Elon Musk',
         'country': 'South Africa'},
    15: {'name': 'Margot Robbie',
         'country': 'Australia'},
    16: {'name': 'Emma Watson',
        'country': 'UK'},
    17: {'name': 'Brad Pitt',
        'country': 'USA'},
    18: {'name': 'Mark Zuckerberg',
         'country': 'USA'},
    19: {'name': 'Johnny Depp',
        'country': 'USA'},
    20: {'name': 'Ellen DeGeneres',
        'country': 'USA'},
    21: {'name': 'Meryl Streep',
        'country': 'USA'},
    22: {'name': 'Shakira',
        'country': 'Colombia'},
    23: {'name': 'Robert Downey Jr.',
        'country': 'USA'},
    24: {'name': 'Gigi Hadid',
        'country': 'USA'},
    25: {'name': 'Chris Hemsworth',
        'country': 'Australia'},
    26: {'name': 'Jennifer Lopez',
        'country': 'USA'},
    27: {'name': 'Justin Bieber',
        'country': 'Canada'},
    28: {'name': 'Demi Lovato',
        'country': 'USA'},
    29: {'name': 'Katy Perry',
        'country': 'USA'},
    30: {'name': 'Denzel Washington',
        'country': 'USA'},
    31: {'name': 'Madonna',
        'country': 'USA'},
    32: {'name': 'Oprah Winfrey',
        'country': 'USA'},
    33: {'name': 'Matthew McConaughey',
        'country': 'USA'},
    34: {'name': 'Zendaya',
        'country': 'USA'},
    35: {'name': 'Tom Holland',
        'country': 'UK'},
    36: {'name': 'Scarlett Johansson',
        'country': 'USA'},
    37: {'name': 'Hugh Jackman',
        'country': 'Australia'},
    38: {'name': 'Emma Stone',
        'country': 'USA'},
    39: {'name': 'Megan Fox',
        'country': 'USA'},
    40: {'name': 'Johnny Depp',
        'country': 'USA'},
    41: {'name': 'Michael Jordan',
        'country': 'USA'},
    42: {'name': 'LeBron James',
        'country': 'USA'},
    43: {'name': 'Robert Pattinson',
         'country': 'UK'},
    44: {'name': 'Miley Cyrus',
        'country': 'USA'},
    45: {'name': 'Tom Cruise',
        'country': 'USA'},
    46: {'name': 'Benedict Cumberbatch',
        'country': 'UK'},
    47: {'name': 'Nicole Kidman',
        'country': 'Australia'},
    48: {'name': 'David Beckham',
        'country': 'UK'},
    49: {'name': 'Eva Mendes',
        'country': 'USA'},
    50: {'name': 'Morgan Freeman',
        'country': 'USA'},
    51: {'name': 'Gwen Stefani',
        'country': 'USA'},
    52: {'name': 'Aishwarya Rai Bachchan',
         'country': 'India'},
    53: {'name': 'Nicole Scherzinger',
        'country': 'USA'},
    54: {'name': 'Justin Timberlake',
        'country': 'USA'},
    55: {'name': 'Blake Lively',
        'country': 'USA'},
    56: {'name': 'Adele',
         'country': 'UK'},
    57: {'name': 'Charlize Theron',
        'country': 'South Africa'},
    58: {'name': 'Eddie Murphy',
        'country': 'USA'},
    59: {'name': 'Ellen Pompeo',
        'country': 'USA'},
    60: {'name': 'Kate Middleton',
        'country': 'UK'},
    61: {'name': 'Prince Harry',
        'country': 'UK'},
    62: {'name': 'Meghan Markle',
        'country': 'USA/UK'},
    63: {'name': 'Tom Brady',
        'country': 'USA'},
    64: {'name': 'Megan Thee Stallion',
        'country': 'USA'},
    65: {'name': 'The Weeknd',
         'country': 'Canada'},
    66: {'name': 'Snoop Dogg',
        'country': 'USA'},
    67: {'name': 'Cardi B',
        'country': 'USA'},
    68: {'name': 'Joe Rogan',
        'country': 'USA'},
    69: {'name': 'Billie Eilish',
        'country': 'USA'},
    70: {'name': 'Harrison Ford',
        'country': 'USA'},
    71: {'name': 'Daisy Ridley',
        'country': 'UK'},
    72: {'name': 'Keanu Reeves',
        'country': 'Canada'},
    73: {'name': 'Jada Pinkett Smith',
        'country': 'USA'},
    74: {'name': 'Chris Pratt',
        'country': 'USA'},
    75: {'name': 'Ryan Reynolds',
         'country': 'Canada'},
    76: {'name': 'Benedict Wong',
        'country': 'UK'},
    77: {'name': 'Priyanka Chopra',
         'country': 'India'}
}

# defining a small function to help clean the returned response text from requests, to help make the regex used below simpler 
def non_english_clean(text):
    accepted = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace
    non_accepted = "[]"
    cleaned_text = ""
    for i in text:
        if i in non_accepted:
            cleaned_text += " "
        elif i in accepted:
            cleaned_text += i
        else:
            continue
    return cleaned_text


# setting the limit for how long the game could go, which is dependant on the number of data provided
count = len(data)

# regex used for filtering data that we'll bring from wikipedia
regex = r"([\w\s\-À-ÿ\"\.,']+)(?:\(|,|\[\d\]).*?(born .*?)\),?(?:[\s\d]+|\s\d|,)?\s(.*?\.)"

# defining the function to collect data from wikipedia if the csv file where the data will be saved doesn't yet exist
# which is usually only done on the first run, so the first run will be taking much longer than the ones after it
def data_collect():

    try:
        for key, celeb_data in data.items():
            name = celeb_data['name']
            response = requests.get("https://en.wikipedia.org/wiki/" + name)
            
            # parsing the response html using beautiful soup with html.parser
            soup = BeautifulSoup(response.text, "html.parser")
            # selecting the information from the parsed html data
            body = soup.body
            body_paragraphs = body.find_all("p")
            bio = str(body_paragraphs[1].text)
            
            # cleaning the information from wikipedia using the function we defined up there and a regex
            bio = non_english_clean(bio)
            description = re.search(regex, bio)
            if description:
                description = description.group(1) + description.group(2) + " " + description.group(3)
            celeb_data["description"] = description

        # I was too lazy to collect the actual follower count, so I used a random number between 100-999
        # this should still be fun to play with XD
        for key, celeb_data in data.items():
            values_list = [str(value) for value in celeb_data.values()]
            # writing all the information to display to the user in a single key
            data[key]["information"] = ", ".join(values_list)
            data[key]["Followers_in_millions"] = random.randint(100, 999)
        return data
    except KeyError:
        print("Key not found")


def higher_lower():
    try:
        with open('higher_lower_game.csv', newline='') as file:
            data = json.load(file)
            for key in list(data.keys()):
                data[int(key)] = data.pop(key)
    except FileNotFoundError:
        data = data_collect()
    # setting local variables to use within the game logic 
    correct_answers = 0
    is_game_over = False
    # using a random number to return a random celebrity from the dict of celebrities we have
    num1 = random.randint(1, count)
    used_nums = [num1]
    while not is_game_over:
        num2 = random.randint(1, count)
        while num2 in used_nums:
            num2 = random.randint(1, count)
        else:
            used_nums.append(num2)
        A = f"{data[num1]["information"]}, followers in millions: {data[num1]["Followers_in_millions"]}"
        B = data[num2]["information"]
        print("A: " + A)
        print("VS")
        print("B: " + B)
        print("Does B have move followers than A: \n")
        answer = input("Choose your answer: type A or B to choose who is higher \n").lower()
        if answer == "a":
            print(f"The Follower count of {data[num2]["name"]} is: \n{data[num2]["Followers_in_millions"]}M ")
            if data[num1]["Followers_in_millions"] > data[num2]["Followers_in_millions"]:
                print("You are correct")
                num1 = num2
                correct_answers += 1
            elif data[num2]["Followers_in_millions"] > data[num1]["Followers_in_millions"]:
                print("You are incorrect! you lost :( ")
                print(f"You got {correct_answers} correct answers!")
                is_game_over = True
        elif answer == "b":
            print(f"The Follower count of {data[num2]["name"]} is: \n{data[num2]["Followers_in_millions"]}M ")
            if data[num2]["Followers_in_millions"] > data[num1]["Followers_in_millions"]:
                print("You are correct")
                num1 = num2
                correct_answers += 1
            elif data[num1]["Followers_in_millions"] > data[num2]["Followers_in_millions"]:
                print("You are incorrect! you lost :( ")
                print(f"You got {correct_answers} correct answers!")
                is_game_over = True
    
    # saving the data collected to a file so it doesn't take too long every time, 
    # if you want to update the information in the file, just delete the file and run the program again 
    try:
        with open("higher_lower_game.csv", 'x') as outfile:  # 'x' mode creates the file if it doesn't exist
            json.dump(data, outfile, indent=4)
        print("Data saved to higher_lower_game.csv")
    except FileExistsError:
        print("higher_lower_game.csv already exists. Skipping save.")


# Launching the game
higher_lower()
