marks = [1, 3, 5, 7, 9]

# alternative of map
doubled_marks = [mark*2 for mark in marks]

print(doubled_marks)

# alternative of filter
max_mark = [mark for mark in marks if mark >3]

print(max_mark)