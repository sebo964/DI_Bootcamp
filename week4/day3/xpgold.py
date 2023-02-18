# # Exercise 1: Birthday Look-Up

# # Instructions

# # Create a variable called birthdays. Its value should be a dictionary.
# # Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# # Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# # Ask the user to give you a person’s name and store the answer in a variable.
# # Get the birthday of the name provided by the user.
# # Print out the birthday with a nicely-formatted message.
bitrhdays = {}
# add 5 random people to the dictionary
bitrhdays["John"] = "1990/01/01"
bitrhdays["Jane"] = "1990/01/02"
bitrhdays["Jack"] = "1990/01/03"
bitrhdays["Jill"] = "1990/01/04"
bitrhdays["Joe"] = "1990/01/05"

print("Welcome to the birthday dictionary. We know the birthdays of:")
input_name = input("Who's birthday do you want to look up? ").capitalize().strip()
print(f"Your birthday is {bitrhdays[input_name]}")


# # Exercise 2: Birthdays Advanced

# # Instructions

# # Before asking the user to input a person’s name print out all of the names in the dictionary.
# # If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)


# # Exercise 3: Add Your Own Birthday

# # Instructions

# # Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# # Ask the user for a person’s name – store it in a variable.
# # Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# # Now add this new data into your dictionary.
# # Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

ask_user_name = input("Please enter a name: ").capitalize().strip()
if ask_user_name in bitrhdays:
    print(f"Your birthday is {bitrhdays[ask_user_name]}")
else:
    ask_user_dob = input("Please enter a date of birth in format YYYY/MM/DD: ")
    bitrhdays[ask_user_name] = ask_user_dob


# # Exercise 4: Fruit Shop

# # Instructions

items = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# print item in items for item price in items.itenms():

for item, price in items.items():
    print(f"{item} costs {price} dollars")
# # Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# # Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# # write some code to calculate how much it would cost to buy everything in stock.
items2 = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1},
}
total = 0
for stock, price_stock in items2.items():
    print(price_stock["price"])
    print(price_stock["stock"])
    total += price_stock["price"] * price_stock["stock"]
print(total)
