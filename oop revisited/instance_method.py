class Person():
    name='Moin'
    def myName(self, name):
        self.name=name

    def overrideMyName(self, name):
        Person.name=name
    
person=Person()
person.myName('Raffian')
print(person.name)
print(Person.name)

# here override name attribute of the Person class
person.overrideMyName('Akalu')
print(person.name)
# Person class name attribute changed to 'Akalu'
print(Person.name)

"""
Instance method can modify and access both class and instance attribute.
"""