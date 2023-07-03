class Person():
    name='Moin'
    @classmethod
    def myName(cls, name):
        cls.name=name


Person.myName('Raffian')
print(Person.name)

"""
Class methods can only access and modify class attributes and not instance attributes
"""