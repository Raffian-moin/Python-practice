person_dictionary = {
    'name': 'moin',
    'age' : 26,
    'is_awesome': True,
}

# accessing the value by key from dictionary
print(person_dictionary['name'])

# if we access value where key doesn't it will throw error
# country key doesn't exist in person_dictionary. so it will throw error
# print(person_dictionary['country'])

# to avoid error we use get()
print(person_dictionary.get('country'))

# add element to the dictionary
person_dictionary['is_funny'] = "Hell yeah"

print(person_dictionary)

# modify element value

person_dictionary['is_funny'] = "Hell funny"

print(person_dictionary)

# deleting element
del person_dictionary['is_funny']

print(person_dictionary)

# looping key value pairs in dictionary

for key, value in person_dictionary.items() :
    print(key, value)

# loop through only keys

for key in person_dictionary.keys() :
    print(key)

# loop through only values

for value in person_dictionary.values() :
    print(value)