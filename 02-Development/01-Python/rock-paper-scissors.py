rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if int(human_choice) == 0:
    print(rock)
elif int(human_choice) == 1:
    print(paper)
elif int(human_choice) == 2:
    print(scissors)
else:
    print("Invalid selection")

computer_choice = random.randint(0, 2)
print("Computer chose:")

if int(computer_choice) == 0:
    print(rock)
elif int(computer_choice) == 1:
    print(paper)
elif int(computer_choice) == 2:
    print(scissors)
else:
    print("Invalid selection")

if computer_choice == human_choice:
    print("It's a draw !!!")
elif human_choice == 0 and computer_choice == 2:
    print(f"{human_choice} wins against {computer_choice}. You win !!!")
elif human_choice == 1 and computer_choice == 0:
    print(f"{human_choice} wins against {computer_choice}. You win !!!")
elif human_choice == 2 and computer_choice == 1:
    print(f"{human_choice} wins against {computer_choice}. You win !!!")
else:
    print(f"{human_choice} loses against {computer_choice}. You lose !!!")
