import pandas

# LIST COMPREHENSION
# Exercise1

# Squared Numbers
# numbers = [1, 2, 49, 45, 5, 3, 23, 34, 4]
# squared_nums = [number*number for number in numbers]
# print(squared_nums)

# Exercise 2

# Even Nums
# even_nums = [num for num in numbers if num % 2 == 0]
# print(even_nums)

# Exercise 3

# Compare two text files and print common numbers
# with open('file1.txt') as f:
#     num1 = f.readlines()
#
# with open('file2.txt') as f:
#     num2 = f.readlines()
#
# common_nums = [int(num) for num in num1 if num in num2]
# print(common_nums)

# DICT COMPREHENSION
# Exercise1

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# Exercise2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
# print(weather_f)

# Phonetic Alphabet Look Up Project
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
{new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
word_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter to word to generate a list : ").upper()
for letter in user_input:
    print(f"{letter} : {word_dict[letter]} ")
