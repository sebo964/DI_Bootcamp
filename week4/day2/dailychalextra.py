# <!-- Instructions

# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !
#  -->

import datetime

bdate = "21/12/1985"
# input("Please enter your birthdate in the format DD/MM/YYYY: ")

bdate = bdate.split("/")
bdate = list(map(int, bdate))

print(bdate)

currenttime = datetime.datetime.now()
currentyear = currenttime.year

print(currentyear)

age = currentyear - (bdate[-1])

print(age)

age = str(age)

age = [*(age)]

age = list(map(int, age))

candles = age[-1]

print(candles)

if bdate[-1] % 4 == 0:
    print("Happy Birthday")
    print("Happy Birthday")
