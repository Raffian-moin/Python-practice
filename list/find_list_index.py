# to find the index of an element by value use index()

cities = ['Bangladesh', 'India', 'Thailand']

print(cities.index('Bangladesh'))

# if the value doesn't exist it will throw error
# following will throw error
# print(cities.index('USA'))

# to avoid error use In
city = 'USA'
if city in cities :
    print(f"The {city} has an index of {cities.index(city)}.")
else:
    print(f"{city} doesn't exist in the list.")