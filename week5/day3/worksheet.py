class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__} : {self.name} {self.age}"


newPerson = Person("Sarah", 24)

print(newPerson)

import collections
