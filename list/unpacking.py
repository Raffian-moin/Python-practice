# If we want to assign list items to individual variables we use Unpacking

colors = ['red', 'green', 'blue']

red, green, blue = colors

# this will throw error as number of variables are less than list items
# colors1, colors2 = colors

# to avoid error
new_colors1, new_colors2, *others = colors


print(red)
print(colors)
print(new_colors1)
print(others)