class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

shepard = Dog('pluto', 10)
native = Dog('kalu', 10)

"""
Instance variable:
==================
instance variable are variables that are tied to a single instance. they are not 
shared by any other instances. that means, if we create a instance of a class,
instance variables of that instance are only tied to that instance. if we create another
instance, it will create it's own same instance variables with different values.
instance variable are created inside constructor or instance method. 
to create instance variable we use: 

self.instance_variable_name
"""

# getting attribute
print('shepard name - '+ shepard.name)
print('shepard name - '+ getattr(shepard, 'name'))

# modifying instance variable
shepard.name = 'juno'
print('shepard name - '+ shepard.name)

print('native name - '+ native.name)

"""
NOTE:
-----
we modified name instance variable to shepard instance.
but name instance variable isn't changed for native instance
"""


# adding instance variable dynamically
shepard.color = 'brown'
print('shepard color - '+ shepard.color)

if hasattr(native, 'color'):
    print(native.color)

"""
NOTE:
-----
we added color instance variable to shepard instance.
but color instance variable doesn't exist in native instance.
"""

# deleting instance variable
del shepard.color
if hasattr(shepard, 'color'):
    print(shepard.color)