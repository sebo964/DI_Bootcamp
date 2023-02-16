
# 🌟 Exercise 1: Import

# Instructions

# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

import datetime
import random
import func as f
import string

add_number = f.func_to_import.add(1, 3)
print(add_number)

# OR


# OR


# OR


# 🌟 Exercise 2: Random Module

# Instructions

# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.


def roll_dice(num):
    random_num = random.randint(1, 100)
    if num == random_num:
        print("Success")
    else:
        print("Try again")


print(roll_dice(3))

# 🌟 Exercise 3: String Module

# Instructions

# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

# datetime module

random_string = []
for i in range(5):
    random_letter = (random.choices(string.ascii_letters))
    i += 1
    random_string.append(random_letter)

print(random_string)


# 🌟 Exercise 4: Current Date

# Instructions

# Create a function that displays the current date.
# Hint: Use the datetime module.


print(datetime.datetime.now())

# Exercise 5: Amount Of Time Left Until January 1st

# Instructions

# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10: 34: 01hours).

Count_down = datetime.datetime(2024, 1, 1) - datetime.datetime.now()

print(Count_down)

# Exercise 6: Birthday And Minutes

# Instructions

# Create a function that accepts a birthdate as an argument ( in the format of your choice), then displays a message stating how many minutes the user lived in his life.


# Exercise 7: Upcoming Holiday

# Instructions

# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is . (Example: the next holiday is in 30 days and 12: 03: 45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

holiday_next = datetime.datetime(2023, 2, 18)

print(datetime.datetime.now())

print(holiday_next - datetime.datetime.now())


# Exercise 8: How Old Are You On Jupiter?

# Instructions

# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1, 000, 000, 000 seconds old, the function should output that they are 31.69 Earth-years old.

person_age = 30
# convert years to seconds
person_age_seconds = person_age * 365.25 * 24 * 60 * 60
# convert seconds to years on earth
person_age_earth = person_age_seconds / 31557600
# convert years to years on mercury
person_age_mercury = person_age_earth / 0.2408467
# convert years to years on venus
person_age_venus = person_age_earth / 0.61519726
# convert years to years on mars
person_age_mars = person_age_earth / 1.8808158
# convert years to years on jupiter
person_age_jupiter = person_age_earth / 11.862615
# convert years to years on saturn
person_age_saturn = person_age_earth / 29.447498
# convert years to years on uranus
person_age_uranus = person_age_earth / 84.016846
# convert years to years on neptune
person_age_neptune = person_age_earth / 164.79132

person_age_earthyears_convert_from_seconds = person_age_seconds / 31557600

# Exercise 9: Faker Module

# Instructions

# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
