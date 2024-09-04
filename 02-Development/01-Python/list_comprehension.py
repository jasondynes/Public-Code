numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

# Write your code 👆 above:

squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)

# filter out even numbers
list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# Use list comprehension to convert the strings to integers 👇:
num_list = [int(nums) for nums in list_of_strings]
print(num_list)

# Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in num_list if num % 2 == 0]

# Write your code 👆 above:
print(result)
