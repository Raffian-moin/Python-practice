class Person:
    name = "moin"

print(Person.name)
print(getattr(Person, 'name'))

# if variable dopesn't exist error throws so use a default varaibele
print(getattr(Person, 'names', 'samad'))

Person.name = "lamichan"
print(getattr(Person, 'name'))

Person.age = 10
print(getattr(Person, 'age'))

# delete class varaible
del Person.age
print(getattr(Person, 'names', 20))


