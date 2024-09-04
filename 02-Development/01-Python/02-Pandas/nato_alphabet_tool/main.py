# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

import pandas
nato_alphabet = pandas.read_csv("../../Day_30/nato_alphabet_tool_2.0_exception_handling/nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Please enter a word to produce NATO phonetics: ").upper()
word_phonetics = [nato_alphabet_dict[letter] for letter in word]
print(f"The NATO phonetic list created is: {word_phonetics}")
