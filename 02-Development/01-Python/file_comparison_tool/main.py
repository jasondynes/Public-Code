# Instructions
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
# 2
# 3
# and file2.txt contained:
#
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.
#
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]
# Hint
# Use the keyword method for starting the List comprehension and fill in the relevant parts.
#
# First, you will need to read from the files and create a list using the lines in the files.
#
# This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
#
# Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp
#
# Remember you can use the int() method in python to convert a string into an integer.

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

# clean lists up and remove \n and convert from string to integer
for i in range(0, len(list1)):
    list1[i] = int(list1[i].strip())
for i in range(0, len(list2)):
    list2[i] = int(list2[i].strip())

result = [num for num in list1 if num in list2]

print(f"Original files are file 1: {list1} \nand file 2: {list2}")

# Write your code above 👆
print(f"\nNumbers that exist in both files are: {result}")
