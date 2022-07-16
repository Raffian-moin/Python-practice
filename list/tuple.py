#assignment is immutable list

colors = ('red', 'green', 'yellow')

# can't assign new item as tuple doesn't allow assignment. following line of will cause error
# colors[3] = "blue"

# we can assign new tuple to existing tuple variable
colors = (1, 3, 5)

print(colors)
print(colors[0])
print(type(colors))