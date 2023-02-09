# 🌟 Instructions

# Given a “Matrix” string:

#     7i3
#     Tsi
#     h%x
#     i #
#     sM
#     $a
#     #t%
#     ^r!

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns, like here:

# 7	i	3
# T	s	i
# h	%	x
# i		#
# s	M
# $	a
# #	t	%
# ^	r	!

# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if/else statements to check the data
# ● String for the output of the secret message

# Hint (if needed) : Look at the remote learning “Matrix” videos for help.

matrix = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"],
]

first_column_words = list(map(lambda x: x[0], matrix))
Only_letters_col1 = list(filter(lambda x: x.isalpha(), first_column_words))
second_column_words = list(map(lambda x: x[1], matrix))
Only_letters_col2 = list(filter(lambda x: x.isalpha(), second_column_words))
third_column_words = list(map(lambda x: x[2], matrix))
Only_letters_col3 = list(filter(lambda x: x.isalpha(), third_column_words))

Decoded_text = (
    "".join(Only_letters_col1)
    + " "
    + " ".join(Only_letters_col2)
    + " "
    + " ".join(Only_letters_col3)
)

print(Decoded_text)

first_column_words2 = []

for i in matrix:
    first_column_words2.append(i[0])

Only_letters_col1_2 = []

for i in first_column_words2:
    if i.isalpha():
        Only_letters_col1_2.append(i)


second_column_words2 = []
for i in matrix:
    second_column_words2.append(i[1])

Only_letters_col2_2 = []
for i in second_column_words2:
    if i.isalpha():
        Only_letters_col2_2.append(i)

third_column_words2 = []

for i in matrix:
    third_column_words2.append(i[2])

Only_letters_col1_3 = []

for i in third_column_words2:
    if i.isalpha():
        Only_letters_col1_3.append(i)

Decoded_text2 = (
    "".join(Only_letters_col1_2)
    + "".join(Only_letters_col2_2)
    + "".join(Only_letters_col1_3)
)

print(Decoded_text2)
