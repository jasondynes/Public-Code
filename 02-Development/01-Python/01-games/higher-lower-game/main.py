import art
import game_data
import random


def random_number():
    number = 0
    while number == number2:
        # number = random.randint(0, len(game_data.data) - 1)
        number2 = random.randint(0, len(game_data.data) - 1)
    return number2


if __name__ == "__main__":
    score = 0
    game_over = False
    print(art.logo)
    number = random.randint(0, len(game_data.data) - 1)
    while not game_over:
        print("------------------------------------------------------------------------------------------------------")
        num1 = num2
        num2 = random_number()
        print(f"Compare A: {game_data.data[num1]['name']}, a {game_data.data[num1]['description']}, from {game_data.data[num1]['country']}")
        print(art.vs)
        print(f"Against B: {game_data.data[num2]['name']}, a {game_data.data[num2]['description']}, from {game_data.data[num2]['country']}")
        if game_data.data[num1]['follower_count'] > game_data.data[num2]['follower_count']:
            right_option = "A"
        elif game_data.data[num1]['follower_count'] < game_data.data[num2]['follower_count']:
            right_option = "B"
        else:
            right_option = "AB"
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == right_option:
            score += 1
        elif answer != right_option and right_option == "AB":
            print("Followers are the same but will give you the point")
            score += 1
        else:
            print("The answer was incorrect. Game Over")
            print(f"The score for this game was {score}")
            game_over = True


