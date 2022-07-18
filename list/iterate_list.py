from turtle import color


colors = ['red', 'green', 'yellow']

for color in colors :
    print(color)

# iterating with index
# this will output with key value pair
for color in enumerate(colors) :
    print(color)

# this will output index
for index, color in enumerate(colors) :
    print(index)