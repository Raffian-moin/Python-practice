class Dog:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color


"""
Class:
======
python class is a blueprint to create objects/instances

syntax:
-------
class className:

constructor:
------------
It is a method which runs every time when create a instance of the class.

__init()__ is the constructor method in python

self:
-----
when we create a instance of the class, instance is passed to the self parameter of the
instance method. so self means current working instance.
self should be the first parameter of the instance method.
self is not a keyword. we can name the first parameter anything we want.

in the example above, in constructor method
self.name means name attribute of the current object is equal name parameter.
the value of name was passed as constructor argument when object was created.
"""