# Exercise 1 : Use The Terminal

# Instructions

# Run this command in the terminal to open a python console:
# $ python3
# Hint: Replace python3 with python for Windows

# Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.
# PATH explanation can be found here.


# Exercise 2 : Alias

# Instructions

# Read about alias, and try to open a python console with the command:
# $ py


# Exercise 3 : Outputs

# Instructions

# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9  # True
#     >>> 3 == 3 == 3 # True
#     >>> bool(0) false
#     >>> bool(5 == "5") # False
#     >>> bool(4 == 4) == bool("4" == "4") # True
#     >>> bool(bool(None)) # False
#     x = (1 == True) # True
#     y = (1 == False) # False
#     a = True + 4  # 5
#     b = False + 10 # 10

#     print("x is", x)
#     print("y is", y)
#     print("a:", a)
#     print("b:", b)


# Exercise 4 : How Many Characters In A Sentence ?

# Instructions

# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velitesse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))


# Exercise 5: Longest Word Without A Specific Character

# Instructions

# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

sen = input("Enter a sentence without the letter A: ")

sen = sen.lower()

sen = [*sen]

sena = None

for i in sen:
    if i == "a":
        sena = False
        break
    else:
        sena = True

if sena == False:
    print("You entered a sentence with the letter A")
else:
    print("Congratulations, you entered a sentence without the letter A")
