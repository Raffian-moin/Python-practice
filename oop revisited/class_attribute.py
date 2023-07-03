class Person():
    counter=0
    def __init__(self, age, name) -> None:
        self.age=age
        self.name=name
        Person.counter+=1


person=Person(4, 'Moin')
person2=Person(4, 'Moin')

print(f"{Person.counter}")

"""
Here counter is the class attribute. it is not tied to any specific instance object.
we can access class attribute from inside instance attribute
"""