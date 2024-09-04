"""############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

"""

import art
import random

def main_game():
    check_continue = "y"
    print(f"Computer's first card: {(computer_cards[0])}")
    while check_continue == "y" and calculate_score(user_cards) <= 21:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        check_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if check_continue == "y":
            user_cards.append(deal_card())

    # deal computer's hand
    while calculate_score(computer_cards) <= 17:
        computer_cards.append(deal_card())
    return


def calculate_score(cards):
    if sum(cards) > 21 and 11 in cards:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def compare_score(user_score, computer_score):
    """ """
    if user_score == 21 and len(user_cards) == 2:
        print("User has Blackjack, you win")
    elif computer_score == 21 and len(computer_score) == 2:
        print("Computer has Blackjack, they win")
    elif user_score > 21 >= computer_score:
        print("You went over. You lose")
    elif user_score <= 21 < computer_score:
        print("Opponent went over. You win")
    elif user_score > 21 and computer_score > 21:
        print("It's a draw as you both went bust")
    elif 21 >= user_score == computer_score and computer_score <= 21:
        if user_score > computer_score:
            print("You win.")
        elif user_score < computer_score:
            print("Computer wins.")
        else:
            print("Computer wins. You lose")
    return


def deal_card():
    """Creates a card list and chooses a card randomly from that"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# main routine
if __name__ == "__main__":
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    """ prompts whether user wants to play a game of Blackjack with valid inputs on y or n"""
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input == "y":
        print(art.logo)
        main_game()
    print(f"Your final hand {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")
    compare_score(sum(user_cards), sum(computer_cards))
