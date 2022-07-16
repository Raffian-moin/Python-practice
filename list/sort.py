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

"""
# SORTED
sort() doesn't return a new list.so we can't assign sorted list to a new value. as a result original list gets changed. but sorted() doesn't modify original list. it returns a new list with changed order
"""

ages = [1, 4, 6, 8, 3]

sorted_ages = sorted(ages)

print(sorted_ages, ages)