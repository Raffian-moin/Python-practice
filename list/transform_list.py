# often times we need to modify list items and re4turn a new list. we can do that with map()

numbers = [1, 2, 3, 6, 8]

def doubleItem(item) :
    return item * 2

# it returs iterator
new_iterators = map(doubleItem, numbers)

# convert iterators to list
new_list = list(new_iterators)

for doubled_value in new_list :
    print(doubled_value)



