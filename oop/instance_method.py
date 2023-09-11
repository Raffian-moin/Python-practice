class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f"hey my name is {self.name} and I'm {self.age} years old.")

    def sound(self, sound):
        self.sound = sound
    
    def modifySound(self, anotherSound):
        self.sound = anotherSound

"""
Instance method:
==================
instance methods are the methods that are tied to a single instance. every
instance of the class has their own copy of instance methods. instance methods 
contains only instance variables.

call instance method:
---------------------
self.instance_method()
"""

shepard = Dog('shepard', 10)
shepard.greet()

# defining instance variable in instance method (not in constructor)
shepard.sound('woof woof')
print(shepard.sound)

# modifying instance variable from another instance method
shepard.modifySound('auuuuu')
print(shepard.sound)