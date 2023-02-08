# 🌟 Exercise 1 : Convert Lists Into Dictionaries

# Instructions

# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
zip_dict = dict(zip(keys, values))

print(zip_dict)


# 🌟 Exercise 2 : Cinemax

# Instructions

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

fees1 = 0

for key, value in family.items():
    if value < 3:
        fees1 += 0
    elif value < 12:
        fees1 += 10
    else:
        fees1 += 15

print(fees1)


Userlistandage = input("Assumeing family name,age,name,age for all family members: ")


Userlistandage = Userlistandage.split(",")
# convert to dictionary

Userlistage = map(int, Userlistandage[1::2])

userlistname = Userlistandage[0::2]

dict_userlistandage = dict(zip(userlistname, Userlistage))

fees2 = 0

for key, value in dict_userlistandage.items():
    if value < 3:
        fees2 += 0
    elif value < 12:
        fees2 += 10
    else:
        fees2 += 15

print(fees2)


# 🌟 Exercise 3: Zara

# Instructions

# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

# ---------------Answer----------------
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand_dict = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

print(brand_dict)

# 3. Change the number of stores to 2.


brand_dict["number_stores"] = 2

# 4. Print a sentence that explains who Zaras clients are.

clients = ", ".join(brand_dict["type_of_clothes"])


print(f"Zara's clients are: {clients}")

# 5. Add a key called country_creation with a value of Spain.

brand_dict.update({"country_creation": "Spain"})


# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.


brand_dict_keys = brand_dict.keys()

if "international_competitors" in brand_dict_keys:
    brand_dict["international_competitors"].append("Desigual")

else:
    print("international_competitors is not in the dictionary")

# 7. Delete the information about the date of creation.

del brand_dict["creation_date"]

# 8. Print the last international competitor.

print(brand_dict["international_competitors"][-1])

# 9. Print the major clothes colors in the US.

print(brand_dict["major_color"]["US"])

# 10. Print the amount of key value pairs (ie. length of the dictionary).

lengthoffidctionary = len(brand_dict)
print(lengthoffidctionary)

# 11. Print the keys of the dictionary.

print(brand_dict.keys())

# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975
# number_stores: 10 000

more_on_zara = {"creation_date": 1975, "number_stores": 10000}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand_dict.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?

# Answer - the value of number of stores was updated to 10000, which is the latest value that was pushed.


# 🌟  Exercise 4 : Disney Characters

# Instructions

# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

# ------------------Answer----------------

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

disney_users_A = dict(enumerate(users))
disney_users_A = {v: k for k, v in disney_users_A.items()}

print(disney_users_A)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# disney_users_B = dict(enumerate(users))

disney_users_B = {}
for i, v in enumerate(users):
    valuetopush = {i: v}
    disney_users_B.update(valuetopush)

print(disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


users_sorted = sorted(users)
disney_users_C = dict(enumerate(users_sorted))
disney_users_C = {v: k for k, v in disney_users_C.items()}


print(disney_users_C)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

for letter_i_users in users:
    if "i" in letter_i_users:
        print(letter_i_users)

print(
    "-------------------------------------------------------------"
)  # just to makre sure the two list are seperate in the answers

for letter_mp_users in users:
    if letter_mp_users.lower().startswith("m") or letter_mp_users.lower().startswith(
        "p"
    ):
        print(letter_mp_users)
