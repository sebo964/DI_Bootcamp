# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

class Circle:
    def __init__(self, radius):
        self.radius = radius
        diameter = radius * 2
        self.diameter = diameter

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def compare(self, other):
        if self.radius > other.radius:
            return f"{self} is bigger than {other}"
        elif self.radius < other.radius:
            return f"{self} is smaller than {other}"
        else:
            return f"{self} is equal to {other}"

    def put_in_list(self, other):
        return [self, other]
