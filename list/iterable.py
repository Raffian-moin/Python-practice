# anything that can be loop over is iterables

# list is iterables
colors = ['red', 'green']

for color in colors :
    print(color)

# string is iterables
name = "moin"

for ch in name :
    print(ch)

# iterator is the agent that performs iteration

colors_iter = iter(colors)
print(next(colors_iter))
# Every time, you call the next() function, it returns the next element in the iterable
print(next(colors_iter))

# iterator is stateful, meaning if we consume the element of the iterator it will get lost
# following will show nothing since we used colors_iter above twice with next() and it became empty. so nothing to iterate
for element in colors_iter :
    print('hello')
    print(element)