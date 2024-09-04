# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
from art import logo, vs
from game_data import data
import random


def random_choice():
    return random.choice(data)


# format data
def format_data(item):
    name = item['name']
    description = item['description']
    country = item['country']
    return f"{name}, {description}, from {country}"


# main game

def game():
    score = 0
    game_over = False
    print(logo)
    choice_a = random_choice()
    while not game_over:
        choice_b = random_choice()
        print(f"Compare A: {format_data(choice_a)}")
        print(vs)
        print(f"Compare B: {format_data(choice_b)}")
        if choice_a['follower_count'] > choice_b['follower_count']:
            right_option = "A"
        elif choice_a['follower_count'] < choice_b['follower_count']:
            right_option = "B"
        else:
            right_option = "AB"
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == right_option:
            score += 1
            choice_a = choice_b
        elif answer != right_option and right_option == "AB":
            print("Followers are the same but will give you the point")
            score += 1
        else:
            print("The answer was incorrect. Game Over")
            print(f"The score for this game was {score}")
            game_over = True


if __name__ == "__main__":
    game()
