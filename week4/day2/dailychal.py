# Instructions

# Challenge 1

# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

usernumber = float(input("Enter a number: "))
userlength = float(input("Enter a length: "))

counteruserlen = 0
usernumber1 = 0
usernumberlist = []

while counteruserlen < userlength:
    usernumber1 = usernumber + usernumber1
    usernumberlist.append(float(usernumber1))
    counteruserlen = counteruserlen + 1

print(usernumberlist)

usernumber1 = usernumber1 == 0


# Challenge 2

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).


stringlist = [*(input("Enter a word: "))]

result = []
last_char = []
for char in stringlist:
    if char != last_char:
        result += char
        last_char = char

fullword = "".join(result)
print(fullword)
