# 🌟 Exercise 1 : Pets

# Instructions

# Using this code:


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.


class Siamese(Cat):
    pass


all_cats = [Bengal("Bengal", 2), Chartreux("Chartreux", 3), Siamese("Siamese", 4)]

sarah_pets = Pets(all_cats)

sarah_pets.walk()


# 🌟 Exercise 2 : Dogs

# Instructions

# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)

    def bark(self):
        return print(f"{self.name} is barking")

    def run_speed(self):
        return int(self.weight) / int(self.age) * 10

    def fight(self, other_dog):
        if int(self.run_speed()) * int(self.weight) > int(other_dog.run_speed()) * int(
            other_dog.weight
        ):
            return print(f"{self.name} won the fight")
        else:
            return print(f"{other_dog.name} won the fight")


dog_1 = Dog("Dog 1", 2, 10)
dog_2 = Dog("Dog 2", 3, 20)
dog_3 = Dog("Dog 3", 4, 30)

dog_1.fight(dog_2)
dog_2.bark()
print(dog_3.run_speed())

# 🌟 Exercise 3 : Dogs Domesticated

# Instructions

# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from xpman import Dog

import random


class Petdog(Dog):
    def __init__(self, name, age, weight, trained=False):
        self.trained = trained
        super().__init__(name, age, weight)

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{args} all play together")

    def do_a_trick(self):
        if self.trained:
            print(
                f"{self.name} {random.choice(['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead'])}"
            )
        else:
            print("Dog is not trained")


pet_dog = Petdog("tobit", 12, 30, trained=True)

pet_dog.do_a_trick()
