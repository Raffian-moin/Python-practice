# if we have a list and we want to perform any action on the items and return only specific items that meets the condition we use filter()

marks = [46, 34, 78, 56, 12]

def checkMark(mark) :
    if (mark > 40) :
        return mark

checked_marks = filter(checkMark, marks)

print(list(checked_marks))

# filter tuples or array of arrays

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

def checkCountry(country) :
    if (country[1] > 300000000) :
        return country

populated = filter(checkCountry, countries)

print(list(populated))