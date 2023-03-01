# We said that NumPy is pretty much a list on steroids. Let’s see that in action.

# For the tasks below, do them using a regular Python list implementation, and then use NumPy.

# Create a table (i.e. a 2d array) of size M x N filled with random integers between 1 and 100,
# where 1 < N < 40 and 1 < M < 50.

# Print out the third row

# Print out the third column

# Set every element in the last row equal to 7

# Set every element in the last column equal the sum of the first two columns. (note: the result of
# the sum is a list which will the same length as the last column)

import numpy as np

table_rand = np.random.randint(
    1, 100, size=(np.random.randint(1, 50), np.random.randint(1, 40))
)


print(table_rand[2])  # Print out the third row
print("------------------")

print(table_rand)

#  print third column
print("------------------")

print(table_rand[:, 2])  # Print out the third column

# set all elements of the last row to 7

table_rand[-1] = 7

print(table_rand)

table_rand[:, -1] = table_rand[:, 0] + table_rand[:, 1]

print(table_rand)
