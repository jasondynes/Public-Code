# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
year_rem_100 = year / 100
year_rem_400 = year / 400

if year % 4 != 0:
    print("Not leap year.")
elif year % 100 == 0 and year % 400 != 0:
    print("Not leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print("Leap year.")
elif year % 100 != 0:
    print("Leap year.")
else:
    print("Not leap year.")
