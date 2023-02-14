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
    def __init__(self, last_name, name, age, gender, is_child):
        self.last_name = last_name
        self.name = name
        self.age = age
        self.gender = gender
        self.is_child = is_child
        self.members = [
            {"Name": name, "age": age, "gender": gender, "is_child": is_child}
        ]

    def born(self, name, gender, familiy):
        self.members.append(
            {"name": name, "gender": gender, "is_child": True, "age": 0}
        )

    print("Congrats on the new born")

    def is_18(self, name, familiy):
        for member in familiy:
            if member["name"] == name:
                if member["age"] >= 18:
                    return True
                else:
                    return False

    def family_presentation(self, familylastnam, family):
        print(familylastnam)
        for member in family:
            print(member["name"])

    def add_family_member(self, name, gender, age):
        is_child = ""
        if int(age) >= 18:
            is_child = "False"
        else:
            is_child = "True"
        self.members.append(
            {"name": name, "gender": gender, "age": age, "is_child": is_child}
        )


family1 = Family("lopez", "Mike", 45, "male", False)
family1.born("paul", "femae", family1.members)
family1.add_family_member("pauline", "male", 57)


print(family1.members)


class Incredibles(Family):
    def __init__(self, last_name, name, age, gender, is_child, power, incredible_name):
        super().__init__(last_name, name, age, gender, is_child)
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
                    Exception("not over 18 years old")
                else:
                    return False

    def incredible_presentation(self, familylastnam, family):
        print(familylastnam)
        for member in family:
            print(member["name"])
            print(member["incredible_name"])
            print(member["power"])
