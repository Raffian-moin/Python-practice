colors_list = ['red', 'yellow', 'yellow']
colors = set(colors_list)

lower_cased = set(map(lambda color: color.upper(), colors))

print(lower_cased)

# alternative

lower_cased = {color.upper() for color in colors}
print(lower_cased)

# with condition
lower_cased = {color.upper() for color in colors if color != 'red'}
print(lower_cased)