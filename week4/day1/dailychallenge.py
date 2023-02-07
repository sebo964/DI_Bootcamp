# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod

word10 = input("Enter a word with 10 characters: ")
word10 = word10.replace(" ", "")

if len(word10) < 10:
    print("String not long enough")
elif len(word10) > 10:
    print("String too long")
else:
    print(word10[0])
    print(word10[-1])

    for i in range(len(word10)):
        print(word10[: i + 1])

    # Bonus
    import random

    word10 = [*(word10)]
    random.shuffle(word10)
    word10 = "".join(word10)
    print(word10)
