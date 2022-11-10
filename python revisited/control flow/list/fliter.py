marks = [1, 5, 6, 7, 10]


# filter(lambda score: score >= 70, scores)
filtered_list = filter(lambda mark: mark> 5, marks)

print(list(filtered_list))