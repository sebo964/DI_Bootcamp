# Instructions

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

input_words = "words,here,separated,by,commas,are,here,but,not,sorted,alphabetically"


sorted_word_list = sorted(input_words.split(","))

new_string = ",".join(sorted_word_list)

print(word for word in sorted_word_list)
