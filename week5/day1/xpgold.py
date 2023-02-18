# Exercise 1 : Geometry

# Instructions

# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.


class circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def print_definition(self):
        print(f"Circle with radius {self.radius}")


# Exercise 2 : Custom List Class

# Instructions

# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
import random


class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse(self):
        return self.letters[::-1]

    def sort(self):
        return sorted(self.letters)

    def random(self):
        return [random.randint(0, 100) for i in range(len(self.letters))]


# Exercise 3 : Restaurant Menu Manager

# Instructions

# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.


# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.
class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        self.menu.append(
            {"name": name, "price": price, "spice": spice, "gluten": gluten}
        )

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                return
        print("Dish not in menu")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                return
        print("Dish not in menu")


menu_list = [
    {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
    {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
    {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
    {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
    {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
]
