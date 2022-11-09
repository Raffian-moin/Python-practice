colors = ['moin', 'klaa','sdd', 'ddd']

colors[1:3] = ['rose', 'summer']
slice_1 = colors[0:2]
slice_2 = colors[:3]
slice_3 = colors[::2]
reversed_list = colors[::-1]
slice_4 = colors[-2:]
del colors[1:3]

print(slice_1)
print(slice_2)
print(slice_3)
print(reversed_list)
print(slice_4)
print(colors)