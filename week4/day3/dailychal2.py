# Instructions

# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

# uncryptedtext = input("Enter a text to encrypt: ")

uncryptedtext = "this is text to encrypt"

# make the aplphabet into a list
aplphabet = "abcdefghijklmnopqrstuvwxyz"
aplphabet = [*aplphabet]

cryptedtext = ""
for letter in uncryptedtext:
    if letter.isalpha() == False:
        cryptedtext += letter
    else:
        # takes the letter, find its index in the aplphabet list, and then adds 3 to it then add it to the crytedtex string variable
        letterindex = aplphabet.index(letter.lower())
        cryptedtext += aplphabet[letterindex - 3]
print(cryptedtext)
