# Exercise 1 : Cars

# Instructions

# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

carmakers = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert it into a list using Python (don’t do it by hand!).

carmakers = carmakers.split(", ")

# Print out a message saying how many manufacturers/companies are in the list.

print(f"there are {len(carmakers)} car manufacturers in the list")

# Print the list of manufacturers in reverse/descending order (Z-A).

carmakers.sort(reverse=True)

print(carmakers)

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

carmaker_o = 0

carmaker_i = 0

for carmaker in carmakers:
    if "o" in carmaker:
        carmaker_o += 1
    if "i" not in carmaker:
        carmaker_i += 1

print(carmaker_i)
print(carmaker_o)

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).

carmaker_dup = [
    "Honda",
    "Volkswagen",
    "Toyota",
    "Ford Motor",
    "Honda",
    "Chevrolet",
    "Toyota",
]
carmaker_remove_dup = set(carmaker_dup)

print(carmaker_remove_dup)

carmaker_remove_dup = list(carmaker_remove_dup)

string_carmaker_remove_dup = ", ".join(carmaker_remove_dup)

print(string_carmaker_remove_dup)

print(len(carmaker_remove_dup))

# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.


# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

sorted_carmaker_remove_dup = sorted(carmaker_remove_dup)

print(sorted_carmaker_remove_dup)

reverseletters = []

for carmaker in sorted_carmaker_remove_dup:
    reverseletters.append(carmaker[::-1])

print(reverseletters)
