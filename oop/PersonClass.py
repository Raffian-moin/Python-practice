class Person:
    counter =  0
    def __init__(self):
        self.name = "moin"
        Person.counter += 1

    def greet(self):
        return "suck your blood"

    @classmethod
    def my_name(cls):
        return "my name is dorbesh"

    @staticmethod
    def getMyName():
        return "hello"

person = Person();

print(person.name)
print(person.counter)

people = Person();
print(people.counter)
print(person.greet())

print(person.my_name())
print(person.getMyName())