# Instructions

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

input_words = "words,here,separated,by,commas,are,here,but,not,sorted,alphabetically"

sorted_words = list(word for word in list(input_words.split(",")))

print(sorted(sorted_words))
