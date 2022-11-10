numbers = ['one', 'two', 'three']

get_index = numbers.index('three')

print(get_index)

# if index doen't exist it will throw error. to avoid this we use IN operator
number = 'onee'
if number in numbers:
    print(numbers.index(number))
else:
    print('not found')
