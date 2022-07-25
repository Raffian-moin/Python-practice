tags = {'python', 'django'}

# map() function
def convertToUppercase(tag) :
    return tag.upper()

uppercase_tags = set(map(convertToUppercase, tags))
print(uppercase_tags)

# alternative: set way

new_uppercase_tags = {tag.upper() for tag in tags}

print(new_uppercase_tags)

# with condition

new_uppercase_tags_1 = {tag.upper() for tag in tags if tag != 'python'}
print(new_uppercase_tags_1) 