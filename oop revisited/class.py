class Person():
    def __init__(self, name, age):
        self.person_name=name
        self.person_age=age

person=Person('Moin', 7)
print(f"Hi, it's {person.person_name}. I'm {person.person_age} years old")

"""
here __init__ function is the instance attribute(function).
meaning it is tied to all objects that are created from Person() class
"""
