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
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(
            f"Congratulations on the new addition to the family! Meet {kwargs['name']}."
        )

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False

    def family_presentation(self):
        print(f"{self.last_name} family members:")
        for member in self.members:
            print(f"- {member['name']}")


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{name}'s power is {member['power']}.")
                else:
                    raise Exception(
                        f"{name} is not over 18 years old and cannot use their power."
                    )
        else:
            print(f"{name} is not a member of the family.")

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredible family members:")
        for member in self.members:
            print(f"- {member['incredible_name']}, who can {member['power']}.")


members = [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False},
]
incredible_members = [
    {
        "name": "Michael",
        "age": 35,
        "gender": "Male",
        "is_child": False,
        "power": "fly",
        "incredible_name": "MikeFly",
    },
    {
        "name": "Sarah",
        "age": 32,
        "gender": "Female",
        "is_child": False,
        "power": "read minds",
        "incredible_name": "SuperWoman",
    },
]

fam = Family("Smith", members)
incredibles = TheIncredibles("Parr", incredible_members)

fam.family_presentation()

incredibles.incredible_presentation()

incredibles.born(
    name="Baby Jack",
    age=0,
    gender="Male",
    is_child=True,
    power="Unknown Power",
    incredible_name="Unknown",
)

incredibles.incredible_presentation()
