import random
art = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/   
"""



def deal_card(times):
    """
    returns a random card from the deck

    :param times: number of times to deal a card
    :return: a random card from the deck
    """
    deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    if times > 1:
        card = [random.choice(deck_of_cards) for _ in range(times)]
    else:
        card = [random.choice(deck_of_cards)]
    return card

def blackjack_sum(cards):
    """
    Performs a blackjack sum calculation

    :param cards: iterable
    :return: sum of iterable within blackjack's rules
    """
    if 1 in cards and (sum(cards) + 10) <= 21:
        index_1 = cards.index(1)
        cards[index_1] = 11
        return sum(cards)
    elif 11 in cards and sum(cards) > 21:
        index_11 = cards.index(11)
        cards[index_11] = 1
        return sum(cards)
    else:
        return sum(cards)

def calculate_final_score(u_score, com_score):
    """
    it calculates the final score of the blackjack game

    :param u_score: int
    :param com_score: int
    :return: str
    """
    if u_score == com_score:
        return "Draw"
    elif com_score == 21:
        return "You lose, computer has blackjack!"
    elif u_score == 21:
        return "You won with a blackjack!"
    elif u_score > 21:
        return "You went over, you lose!"
    elif com_score > 21:
        return "computer went over, you win!"
    elif u_score > com_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack():
    """
    it is a function that plays the blackjack game

    :return: none
    """
    your_score = 0
    computer_score = 0
    is_game_over = False
    # deal cards
    your_cards = deal_card(2)
    computer_cards = deal_card(2)

    # Game logic
    while not is_game_over:
        your_score = blackjack_sum(your_cards)
        computer_score = blackjack_sum(computer_cards)
        print(f"Your cards: {your_cards} current_total: {your_score}")
        print(f"Computer first card: {[computer_cards[0]]}")
        if your_score == 21 or computer_score == 21 or your_score > 21:
            is_game_over = True
        else:
            # user dealing
            another_card = input("Type 'y' to get another card or 'n' to pass: \n")
            if another_card == "y":
                your_cards += deal_card(1)
            else:
                is_game_over = True
    # displaying computer's hidden card
    print(f"Computer's second card:  {computer_cards}")
    while computer_score != 21 and computer_score < your_score < 21:
            # computer dealing
            print("Computer draws a card")
            computer_cards += deal_card(1)
            computer_score = blackjack_sum(computer_cards)

    print(f"Your final hand {your_cards} final score: {your_score}")
    print(f"Computer final hand {computer_cards} final score: {computer_score}")
    return calculate_final_score(your_score, computer_score)

while True:
    play = input("Do you want to play a game of blackjack? type 'y' or 'n': \n")
    if play.lower() == 'y':
        print("\n\n\n\n\n\n\n\n\n")
        print(art)
        print(blackjack())
    else:
        print("Goodbye!")
        break
