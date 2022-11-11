colors_list = ['red', 'yellow', 'yellow']
colors = set(colors_list)

print(colors)
print(len(colors))

colors.add('green')
print(colors)

# adding duplicate color
colors.add('green')
print(colors)

colors.remove('green')
print(colors)

# remove() causes error if value doesnt exist so we have to use discard()
print("===========")
print(colors)
colors.discard('green')
print(colors)

print("===========")
# remove and return an element
color = colors.pop()
print(color)


print("===========")

for value in colors:
    print(value)

print("===========")
for index, value in enumerate(colors):
    print(f"{index}: {value}")
    

print("===========")
colors.clear()
print(colors)

colors_list = ['red', 'yellow', 'yellow']
colors = set(colors_list)

print("===========")
frozen_colors = frozenset(colors)
# frozen_colors.add('colors')
print(frozen_colors)


