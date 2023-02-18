# Exercise 1 : Family

# Instructions

# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.


# Exercise 2 : TheIncredibles Family

# Instructions

# Create a class called TheIncredibles. This class should inherit from the Family class:

# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.


# Member1 = {"name": "Michael", "age": 35, "gender": "Male", "is_child": False}
# Member2 = {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False}
# family_memmbers = [Member1, Member2]


# def born(name, gender, familiy):
#     familiy.append({"name": name, "gender": gender, "is_child": True, "age": 0})
#     print("Congrats on the new born")


# def is_18(name, familiy):
#     for member in familiy:
#         if member["name"] == name:
#             if member["age"] >= 18:
#                 return True
#             else:
#                 return False

# def family_presentation(familylastnam, family):
#     print(familylastnam)
#     for member in family:
#         print(member["name"])


# born("jack", "male", family_memmbers)

# print(family_memmbers)


class Family:
    def __init__(self, **kwargs):
        self.last_name = kwargs["last_name"]
        self.name = kwargs["name"]
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.is_child = kwargs["is_child"]

    def born(self, name, gender):
        self.members.append(
            {"name": name, "gender": gender, "is_child": True, "age": 0}
        )

        print("Congrats on the new born")

    def is_18(self):
        for member in self.members:
            if member["name"] == self.name:
                if member["age"] >= 18:
                    return True
                else:
                    return False

    def family_presentation(self, familylastnam):
        print(familylastnam)
        print(self.name)

    def add_family_member(self, name, gender, age):
        is_child = ""
        if int(age) >= 18:
            is_child = "False"
        else:
            is_child = "True"
        self.members.append(
            {"name": name, "gender": gender, "age": age, "is_child": is_child}
        )


Family_1 = [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False},
]

Family.family_presentation(Family_1, "TheIncredibles")


class Incredibles(Family):
    def __init__(self, last_name, name, age, gender, is_child, power, incredible_name):
        Family.__init__(last_name, name, age, gender, is_child)
        self.power = power
        self.incresible_name = incredible_name
        self.members = [
            {
                "Name": last_name,
                "name": name,
                "age": age,
                "gender": gender,
                "is_child": is_child,
                "power": power,
                "incredible_name": incredible_name,
            }
        ]

    def use_power(self, name, familiy):
        for member in familiy:
            if member["name"] == name:
                if member["age"] >= 18:
                    return True
                else:
                    return False
        Exception("not over 18 years old")

    def incredible_presentation(self, familylastnam, family):
        print(familylastnam)
        for member in family:
            print(member["name"])
            print(member["incredible_name"])
            print(member["power"])
