class Dog:
    def __init__(self, name) -> None:
        self.name = name

    @staticmethod
    def dogType(type):
        match type:
            case 'shepard':
                print('Dog is shepard')
            case 'native':
                print('Dog is native')

    def checkDogType(self, type):
        # calling static method inside instance method
        self.dogType(type)


# accessing static method
# className.staticMethod()
Dog.dogType('shepard')


native = Dog('pluto')
# accessing static method via instance method
native.checkDogType('shepard')

"""
Static method:
==============
Static methods are methods that are not bound to class or instance of the 
class. meaning that, static methods don't use class or instance variables and
methods. they are used for defining utility methods or group functions that have 
some logical relationships in a class. if we want to access class variable or instance
variable for static method, we may need class or instance method, not static method.

Syntax:
-------
@staticmethod
"""