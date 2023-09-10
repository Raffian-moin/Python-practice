class Dog:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

shepard = Dog('shepard', 'black')
print(shepard.name)

# mutating instance attribute
shepard.name = 'native dog'
print(shepard.name)

"""
Instance:
=========
Instantiate an Object/Instance:
-------------------------------
instanceName = className(constructor parameters (if exists))

getting instance attribute:
---------------------------
instanceName.attribute_name
"""