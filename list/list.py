numbers = [1, 3, 7, 9, 2, 4];
# modify value by index
numbers[3] = 10 

# insert at the end
numbers.append(20)
print(numbers)

# remove from the end. it can also return removed value
numbers.pop()
second = numbers.pop(2)
print(second)

# insert at the end
numbers.insert(2, 27)
print(numbers)

# delete at any posotion
del numbers[2]
print(numbers)


numbers.append(4)
print(numbers)

# remove by value. but array has multiple items with same value only first item gets deleted
numbers.remove(4)
print(numbers)

# get item from start by index
print(numbers[1])
# get item from end by index
print(numbers[-1])


