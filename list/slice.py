colors = ['red', 'yellow', 'green', 'blue']

# slice from start to before the specified number
print(colors[0:2])

# slice upto first nth items from start
print(colors[:3])

# slice upto first nth items from end
print(colors[-3:])

# slice nth step. starting from first one then specified step number
print(colors[::2])
print(colors[::3])

# reverse the list. sort() function reverse the list alphabatically but it's reverse the way list is placed
print(colors[::-1])

# add new items to the list and replace specified items
colors[0:2] = ['black', 'violet']
print(colors)

# delete specified items
del colors[0:2]
print(colors)

# replace to specified numbers of itemms and add new extra items after them
colors[0:2] = ['sky-blue', 'maroon', 'white']
print(colors)