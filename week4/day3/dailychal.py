# Challenge 1

# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}


userword = input("Enter a word: ")

valid = True
for char in userword:
    if char.isalpha() == False:
        valid = False
        break
    else:
        valid = True


def userworddict(userwordlist):
    from collections import defaultdict

    userworddict = defaultdict(list)

    # sets the default value of the dictionary to a list so we can push mutiple values to the same key in the loop

    for index, char in enumerate(userwordlist):
        # enumerate returns the index and the value of the list
        # pushes the character to the dict and the index to the value list for the that key
        # loop for all letters in the word
        userworddict[char].append(index)

    # sets the dict to a normal dict so we can print it without the defaultdict artifacts

    userworddict = dict(userworddict)

    print(userworddict)


if valid == True:
    userwordlist = [*(userword)]
    userworddict(userwordlist)
else:
    print("Invalid input")
    exit()

# Challenge 2

# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100"

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1"

# ➞ "Nothing"

#  ---------------------Answer------------------------

# code is valid only if the curreny in the wallet and the currency of the items is the same.

# -----------INPUT -----------------------
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"

# ----------------INPUT--------------------


def value(currency):
    import re

    value = re.findall(
        "[0-9]+", currency
    )  # removes the $ from the wallet value and returns an int
    value = "".join(value)  # joins the list into a string
    intvalue = int(value)  # converts the string to an int
    return intvalue


# print(value(wallet))

value_of_item = items_purchase.values()

int_value_of_item = []

# print(value_of_item)

for item in value_of_item:
    int_value_of_item.append(value(item))

# print(int_value_of_item)

what_can_i_afford = []

for itemcheck in int_value_of_item:
    if itemcheck <= value(wallet):
        what_can_i_afford.append(itemcheck)

# print(what_can_i_afford)

name_of_whats_affordable = []

for key, item in items_purchase.items():
    name_of_whats_affordable.append(key)

# print(name_of_whats_affordable)

name_of_whats_affordable = sorted(name_of_whats_affordable)

print(name_of_whats_affordable)
