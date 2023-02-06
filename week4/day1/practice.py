print(type(str(100)))


from datetime import date

birth_year = input("What year were you born? ")
if len(birth_year) != 4:
    print("Invalid year")
elif (int(birth_year) < 1900) or (int(birth_year) > date.today().year):
    print("Invalid year")
else:
    age = date.today().year - int(birth_year)
    print(f"You are {age} years old")

import random
