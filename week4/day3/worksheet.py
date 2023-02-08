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


# ---------------------Answer------------------------

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
