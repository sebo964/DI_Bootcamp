# 🌟 Exercise 1 – Random Sentence Generator

# Instructions

# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

import random

word_list = []

input_file = "week5/day4/xpman/sowpods.txt"

words_selected = []
# open the input_file and read the content, append every word to the word_list, then close the file


# select 5 words from the word_list and store them in a variable called words_selected
def get_random_sentence(length):
    with open(input_file) as f:
        for line in f:
            word_list.append(line.strip())
        words_selected = random.sample(word_list, length)
        return print(" ".join(words_selected).lower())


# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

input_length = input("How long do you want the sentence to be? (2-20)")
if input_length.isdigit():
    input_length = int(input_length)
    if input_length >= 2 and input_length <= 20:
        get_random_sentence(input_length)
    else:
        print("Please enter a number between 2 and 20")

# 🌟 Exercise 2: Working With JSON

# Instructions

import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

sampleJson = json.loads(sampleJson)

sampleJson["company"]["employee"]["birth_date"] = "01/01/2000"
value_salary = sampleJson["company"]["employee"]["payable"]["salary"]
print(value_salary)

json.dump(sampleJson, open("week5/day4/xpman/sampleJson.json", "w"))
