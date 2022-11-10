marks = [1, 2, 3, 4]

def double(mark):
    return mark*2

new_list = map(double, marks)

print(list(new_list))