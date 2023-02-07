# 🌟 Exercise 1 : Set

# Instructions

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1, 2, 3, 5, 6}
my_fav_numbers.add(12)
my_fav_numbers.add(10)

my_fav_numbers = set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)

friend_fav_numbers = {9, 8, 6}

print(friend_fav_numbers)

total_list_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(total_list_fav_numbers)

# 🌟 Exercise 2: Tuple

# Instructions

# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# Ansvwer: tuples cannoit be changed, so no addition is possible.


# 🌟 Exercise 3: List

# Instructions

# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

listbasket = ["Banana", "Apples", "Oranges", "Blueberries"]

listbasket.remove("Banana")
listbasket.remove("Blueberries")
listbasket.append("Kiwi")
listbasket.insert(0, "Apples")

print(listbasket)

counterofapples = 0
listloop = 0

for app in listbasket:
    if app == "Apples":
        counterofapples = counterofapples + 1

print(counterofapples)


# 🌟 Exercise 4: Floats

# Instructions

# Recap – What is a float? What is the difference between an integer and a float?

# Answer - float is a decimal value, integers are whole numbers

# Can you think of another way to generate a sequence of floats?

# Answer:  there are many ways such as using loops // did not understand tge question.

# generate random numbers and formatting them to floats.

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

thelist = []
num = 1
while num < 5:
    num = num + 0.5
    thelist.append(num)

print(thelist)


# 🌟 Exercise 5: For Loop

# Instructions

# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

numex5 = 0
numex5_list = []


while numex5 < 20:
    numex5 = numex5 + 1
    print(numex5)
    numex5_list.append(numex5)

for x in numex5_list:
    x = x + 1
    if x % 2 == 0:
        print(x)

# 🌟 Exercise 6 : While Loop

# Instructions

# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

userinput = input("Enter Your name: ")

while userinput != "seb":
    userinput = input("enter Your name: ")


# 🌟 Exercise 7: Favorite Fruits

# Instructions

# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

userfruits1 = input("Add your fruits ")
userfruits_list = [userfruits1.split(" ")]
print(userfruits_list)

userfruits2 = input("Add any fruit name ")

for x in userfruits_list:
    if userfruits2 == x:
        print("You chose one of your favorite fruits! Enjoy!")

print("You chose a new fruit. I hope you enjoy ")


# Exercise 8: Who Ordered A Pizza ?

# Instructions

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

usertopping = input("Add your toppings ")
topping_count = 0
while usertopping != "quit":
    usertopping = input("Add your toppings ")
    print("you will add that topping to their pizza ")
    topping_count = topping_count + 1


totalprice = 10 + (2.5 * topping_count)
print(f"all the toppings on the pizza pie and what the total price is {totalprice} ")

# Exercise 9: Cinemax

# Instructions

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

price = []

listfamages = input(
    "Enter the name of each person who needs ticket seperated by comma: "
)


listfamages = listfamages.split(",")
listfamages = list(map(int, listfamages))
print(listfamages)


print(len(listfamages))


for age in listfamages:
    if age < 3:
        price.append(0)
    elif age >= 3 and age <= 12:
        price.append(10)
    elif age > 12:
        price.append(15)

print(sum(price))


# Exercise 10 : Sandwich Orders

# Instructions

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = [
    "Tuna sandwich",
    "Avocado sandwich",
    "Egg sandwich",
    "Sabih sandwich",
    "Pastrami sandwich",
]

sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print("Deli has run out of pastrami.")

finished_sandwiches = []

for sand in sandwich_orders:
    finished_sandwiches.append(sand)

for sandfin in finished_sandwiches:
    print(f"I nmade your {sandfin}.")

# Exercise 11 : Sandwich Orders#2

# Instructions

# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
