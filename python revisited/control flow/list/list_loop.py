numbers = ['one', 'two', 'three', 'four']

for number in numbers:
    print(number)

# with index in a tuple fashion

for number in enumerate(numbers):
    print(number)

# with index
for index, number in enumerate(numbers):
    print(f"{index}: {number}")
