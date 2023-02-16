# # Instructions :

# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

import translate as tr

test_string = "A good book would sometimes cost as much as a good house."


# Part I

# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code


# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        return self.text.count(word)

    def most_common_word(self):
        max(self.text.split(), key=self.text.count)

    def unique_words(self):
        return set(self.text.split())

    @classmethod
    def from_file(cls, file):
        with open(file) as f:
            return f.read()


# Now, use the provided test_string and try using the class you created above.

Word_count = Text(test_string)

word_freq = Word_count.word_frequency("good")

# print(word_freq)

albert = Text.from_file("week5/day4/testtextday4.txt")

# print(albert)

# Part II

# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.


# Bonus:

# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
        self.text = text
        self.list = text.split(" ")

    def no_punctuation(self):
        # remove punctuation
        return (
            self.text.replace(".", "")
            .replace(",", "")
            .replace("!", "")
            .replace("?", "")
        )

    def no_stop_words(self, file2):
        # remove stop words
        file2_read = Text.from_file(file2)
        # from file2 remove all the words in file1
        for word in file2_read.split():
            self.text = self.text.replace(word, "")

        return self.text

    def trans(self):
        # translate to english
        translation_to_fr = tr.Translator(to_lang="fr")
        return translation_to_fr.translate(self)


# save the translated french version of testtextday4.txt to a new file called testtextday4fr.txt

TextModification.trans(
    TextModification.from_file("week5/day4/testtextday4.txt")
).to_file("week5/day4/testtextday4fr.txt")
