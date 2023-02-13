# 🌟 Exercise 2 : Dogs

# Instructions

# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)

print(davids_dog.name, davids_dog.height)

davids_dog.bark()
davids_dog.jump()

sarah_dog = Dog("Teacup", 20)

print(sarah_dog.name, sarah_dog.height)

sarah_dog.bark()
sarah_dog.jump()

list_of_dogs = [davids_dog, sarah_dog]


def bigger_dog(list_of_dogs):
    bigger_dog = list_of_dogs[0]
    for dog in list_of_dogs:
        if dog.height > bigger_dog.height:
            bigger_dog = dog
    return bigger_dog


print(f"Bigger dog is {bigger_dog(list_of_dogs).name}")

print("_______________")

print(davids_dog.name, davids_dog.height, davids_dog.bark(), davids_dog.jump())
