# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
scrambled_password = ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for n in range(0, nr_letters):
    password += random.choice(letters)

for n in range(0, nr_numbers):
    password += random.choice(numbers)

for n in range(0, nr_symbols):
    password += random.choice(symbols)

""""# pop list to shuffle method
for n in range(0, len(password)):
    scrambled_password += password.pop(random.randint(0, len(password) - 1))"""

# random shuffle method
random.shuffle(password)
scrambled_password = "".join(password)

print(f"Here is your password shuffled using this Python Method: {scrambled_password}")
