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

print("-------------------------------------------------------------")

for letter_mp_users in users:
    if letter_mp_users.lower().startswith("m") or letter_mp_users.lower().startswith(
        "p"
    ):
        print(letter_mp_users)
