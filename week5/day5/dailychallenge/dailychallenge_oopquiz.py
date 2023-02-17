# Instructions

# Part 1 : Quizz :

# Answer the following questions

# What is a class?

# A class is a blueprint for creating objects, the class can be used to create instances of objects using parameters passed during invocation. The class can also be used to create methods that can be used by the instances of the class.

# What is an instance?

# instances are objects created from a class. They are created using the class name and passing in the parameters required by the class.

# What is encapsulation?

# Encapsulation is the process of making sure that the attributes of a class are not accessible from outside the class. This is done by using dunder methods to make the attributes private.

# What is abstraction?

# abstraction is the process of planning what will be made private through encapsulation.

# What is inheritance?

# Inheritance is the process of creating a class that inherits from another class. The class that is inherited from is called the parent class and the class that inherits from it is called the child class.

# What is multiple inheritance?

# this is the case where a class inherits from more than one parent class.

# What is polymorphism?

# POLYMORPHISM is the process of using the same method name for different classes. This is done by using the same method name for different classes.

# What is method resolution order or MRO?

# MRO is the order in which the methods are searched for in a class hierarchy.


# Part 2: Create A Deck Of Cards Class.

# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

suit = ["Heart", "Diamond", "Club", "Spade"]

deck_cards = []

# for each card assign a suit a card and store in deck_cards

# for card in cards:
#     for shape in suit:
#         deck_cards.append((card, shape))


# # shuffle the deck of cards using the random module

# shuffled_deck = []

# for i in range(len(deck_cards)):
#     random_selected = random.randint(0, len(deck_cards) - 1)
#     shuffled_deck.append(deck_cards[random_selected])


# def deal(shuffled_deck):
#     random_selected_deal = random.randint(0, len(shuffled_deck) - 1)
#     card_deal = shuffled_deck[random_selected_deal]
#     print(card_deal)
#     return shuffled_deck.pop(random_selected_deal)


# deal(shuffled_deck)


class Card:
    def __init__(self, suit, card):
        self.suit = suit
        self.value = card
        self.deck_cards = deck_cards

    def build_card(self, deck_cards):
        for card in cards:
            for shape in suit:
                deck_cards.append((card, shape))


class Deck:
    def __init__(self, deck_cards):
        self.deck_cards = deck_cards

    def shuffle(self, deck_cards, shuffled_deck):
        for i in range(len(deck_cards)):
            random_selected = random.randint(0, len(deck_cards) - 1)
            shuffled_deck.append(deck_cards[random_selected])
        return shuffled_deck

    def deal(self, shuffled_deck):
        random_selected_deal = random.randint(0, len(shuffled_deck) - 1)
        card_deal = shuffled_deck[random_selected_deal]
        print(card_deal)
        return shuffled_deck.pop(random_selected_deal)


card2 = Card(suit, cards)
card2.build_card(deck_cards)

print(deck_cards)

shuffle_deck1 = []

deck1 = Deck(deck_cards)
deck1.shuffle(deck_cards, shuffle_deck1)

print(shuffle_deck1)

deck1.deal(shuffle_deck1)

print(len(shuffle_deck1))

deck1.deal(shuffle_deck1)

print(len(shuffle_deck1))
