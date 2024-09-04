# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_count = 0
name2_count = 0
name1 = name1.lower()
name2 = name2.lower()

name1_count = name1_count + name1.count("t") + name2.count("t")
name1_count = name1_count + name1.count("r") + name2.count("r")
name1_count = name1_count + name1.count("u") + name2.count("u")
name1_count = name1_count + name1.count("e") + name2.count("e")

name2_count = name2_count + name1.count("l") + name2.count("l")
name2_count = name2_count + name1.count("o") + name2.count("o")
name2_count = name2_count + name1.count("v") + name2.count("v")
name2_count = name2_count + name1.count("e") + name2.count("e")

number = int(str(name1_count) + str(name2_count))
# number = int(number)

if number < 10 or number > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif 40 <= number <= 50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.")
