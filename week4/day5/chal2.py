# Exercise 1

# Instructions

# Draw the following pattern using for loops:
#   *
#  ***
# *****


# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****


# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *


# Exercise 2

# Instructions

# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):  # i = 0, 1, 2, 3 - loops in the list
    minimum = i  # assigns the value of i to minimum
    for j in range(
        i + 1, len(my_list)
    ):  # second loops in the list but the range is now 1 less, it starts from position 1 instead or 0 in the above
        if (
            my_list[j] < my_list[minimum]
        ):  # if the value of the second loop is less than the value of the first loop assign j value to the minimum variable
            minimum = j
            if (
                minimum != i
            ):  # if the minimum value is not equal to the value of i then swap the values
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)  # prints the list in ascending order

# Ans: the program sorts a list of numbers in ascending order.
