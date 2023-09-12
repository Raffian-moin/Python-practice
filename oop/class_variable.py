class Dog:
    scientific_name = 'Canis lupus familiaris'

    def __init__(self) -> None:
        pass

    def introduction(self, name):
        self.name = name
        print(f"my name is {self.name} and my scientific name is {Dog.scientific_name}")

shepard = Dog()
native = Dog()

# modify class variable via instance
shepard.scientific_name = 'hijijbi'

# access class variable
print(shepard.scientific_name)
print(native.scientific_name)

# modify class variable via class
Dog.scientific_name = 'kukur familaries'

# this instance won't get the new value modified via class
print(shepard.scientific_name)
# this instance will get the new value modified via class
print(native.scientific_name)

# but when we access class variable via class it will always return the fresh value
# whether instance of the class modified the class variable or not
shepard.introduction('pluto')
native.introduction('kalu')

"""
Class variable:
===============
class variables are variables the are not tied to any specific instance. they 
are shared with all instances. when we need a value that is common to all instances
we should use class variables.

class variables can access with 
1. self.class_variable
2. className.class_variable

modifying class variable:
-------------------------
when modifying class variable using instance it doesn't actually modify the class variable.
it creates a new instance variable and store value to that variable.
if we then change the class variable using class syntax, class variable will be modified.
but instance that changed the class variable will not get the new value modified via class
because instance already has that variable and it will take preference.
"""