# Reverse The Sentence

# Write a program to reverse the sentence wordwise.

# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You


# sentence = input("Enter a sentence: ")

sentence = "You have entered a wrong domain"

sentence_word_list = sentence.split(" ")

sentence_word_list.reverse()

print(" ".join(sentence_word_list))
