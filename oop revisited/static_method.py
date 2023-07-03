class Person():
    def myAge(self, age):
        self.age=age

    @staticmethod
    def checkAge(age):
        if age>17:
            return 'Adult'
        else:
            return 'Not adult'

print(Person.checkAge(17))
myAgeObj=Person()
myAgeObj.myAge(45)
print(Person.checkAge(myAgeObj.age))

"""
static method is used for logical grouping. It can't access or modify class or instance
attributes, hence cls or self is not passed to the static method
"""