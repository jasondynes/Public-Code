# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# Text to ASCII generator used is https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

import random
import clear


def art():
    print("""
       ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____           ____      _      __  __  U _____ u 
    U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u     U /"___|uU  /"\  uU|' \/ '|u\| ___"|/ 
    \| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/     \| |  _ / \/ _ \/ \| |\/| |/ |  _|"   
     | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <        | |_| |  / ___ \  | |  | |  | |___   
      \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\        \____| /_/   \_\ |_|  |_|  |_____|  
      _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_       _)(|_   \\    >><<,-,,-.   <<   >>  
     (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)     (__)__) (__)  (__)(./  \.) (__) (__) 
""")
    return


def initialise():
    """function will return attempts based on a selection of 'easy' or 'hard' """
    clear.clear()
    art()
    print("Welcome to the number guessing game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("invalid choice")
        initialise()
    return attempts


def main_game(max_attempts):
    attempts = max_attempts
    number = random.randint(1, 100)
    for _ in range(max_attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        number_guess = int(input("Make a guess: "))
        attempts -= 1
        if number_guess > number:
            print("Too high.\nGuess again.")
        elif number_guess < number:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {number}")
            break
    if number_guess != number and attempts == 0:
        print("You have run out of attempts. You lose")
    return


if __name__ == "__main__":
    guesses = initialise()
    main_game(guesses)
