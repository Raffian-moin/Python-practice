class Dog:
    scientific_name = 'Canis lupus familiaris'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def change_scientific_name(cls):
        cls.scientific_name = 'kukur'

    @classmethod
    def native_dog(cls):
        return cls('kalu', 36)


print(Dog.scientific_name)

# modifying class variable
Dog.change_scientific_name()
print(Dog.scientific_name)

shepard = Dog('pluto', 26)
print(shepard.name, shepard.age)

# returning class instance from class method
native = Dog.native_dog()
print(native.name)
print(native.age)

"""
Class Method:
============
class methods are not bound to any instance of the class. they are
shared by all class instances. class methods are used to work with
class variables. we can also return class instance from class methods.
not that, we can define multiple class methods in the class.
"""