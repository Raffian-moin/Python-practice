from functools import reduce

marks = [1, 2, 3, 4, 5]
sum = 0
total = reduce(lambda a, b: a+b, marks)

print(total)