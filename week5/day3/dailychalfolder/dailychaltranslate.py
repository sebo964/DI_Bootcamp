# Instructions:

# Consider this list

import translate

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# Look at this result:
# {"Bonjour": "Hello", "Au revoir": "Goodbye",
#     "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.


def translate_word(word):
    translated_words = []
    for word in word:
        translator = translate.Translator(to_lang="English")
        translated_words.append(translator(word))
    print(translated_words)
