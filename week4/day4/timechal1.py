# Count Occurence

# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3


# String: This is a great example
# Character: y
# 0


string_input = "string"
char_input = "i"


def count_occurence(string_input, char_input):
    count = 0
    for char in string_input:
        if char == char_input:
            count += 1
    return print(count)


count_occurence(string_input, char_input)
