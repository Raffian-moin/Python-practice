students = {
    'name': 'moin'
}

print(students['name'])
print(students.get('name'))

# add a new key value pair
students['age'] = 10
print(students)

# modify 
students['age'] = 15
print(students)

# remove key value pair
del students['age']
print(students)

# iterate over dictionary

for key, value in students.items():
    print(f"{key} : {value}")

# only loop through keys
for key in students.keys():
    print(key)

# looping through keys is the default behavour. so don't need to use keys()

for key in students:
    print(key)

# loop through values
for student in students.values():
    print(student)
