# python by default sorts number items from small to big and strings A-Z chronologically
numbers_ascending = [9, 8, 7, 6, 5, 4, 3, 2, 1]
numbers_descending = [1, 2, 3, 4, 5, 6,]

numbers_ascending.sort()
numbers_descending.sort(reverse=True)

print(numbers_ascending)
print(numbers_descending)

# sort list of tuples

companies = [
    ('google', 123),
    ('tesla', 900),
    ('technovista', 345),
]

def sort_key(company) :
    return company[1]

companies.sort(key= sort_key, reverse=True)

print(companies)