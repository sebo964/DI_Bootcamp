# 🌟 Exercise 1 : What’s Your Name ?

# Instructions

# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.


def get_full_name(first_name, last_name, middle_name=""):
    print(f"{first_name} {middle_name}{last_name}")


get_full_name("john", "wayne")
# Exercise 2 : From English To Morse

# Instructions

# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.

morse_to_text = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "--..--": ",",
    ".-.-.-": ".",
    "..--..": "?",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".--.-.": "@",
    "-....-": "-",
    "-...-": "=",
    ".----.": "'",
    "---...": ":",
    "-.-.--": "!",
    "-.--.": "'",
    "-..-": "X",
    "-.-.-.": ";",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    ".-.-.": "+",
}

translation_to_morse = []

words_to_translate = "This is a text to transalte to morse code, SOS."


def to_morse(word_to_translate):
    # split words_to_translate to indvidual words
    list_of_words = word_to_translate.split(" ")
    for word in list_of_words:
        char_list = [*word]
        for char in char_list:
            char = char.upper()
            # return the key for a value char
            for key, value in morse_to_text.items():
                if char == value:
                    translation_to_morse.append(key)
                    translation_to_morse.append(" ")
                    print(key, end=" ")


to_morse(words_to_translate)


# 🌟 Exercise 3 : Box Of Stars

# Instructions

# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

box_printer = "\nHello\n, \nWorld\n, \nin\n, \nreallylongword\n, \na\n, \nframe\n"

# add new line to each string
box_printer = box_printer.replace(",", "")

box_printer = box_printer.replace(" ", "")

box_printer_list = list(box_printer.split("\n"))

longest_word = []

for i in len(box_printer_list):
    if len(box_printer_list[i]) > len(box_printer_list[i + 1]):
        longest_word = box_printer_list[i]
print(longest_word)

len_longest_word = 0


# 🌟 Exercise 4

# Analyse this code before executing it. What is the purpose of this code?
# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)
