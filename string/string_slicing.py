# string[start:end]
# While slicing string start position is always inclusive but end is not inclusive
s='abcdefghijklmnopqrstupwxyz'

#Take first 4 characters
print(s[:4])

#Take last characters after first 4 characters
print(s[4:])

# Here indexed 3 character is included but indexed 7 isn't included
print(s[3:7])

# Negative Indexing
# Here starting position is index 6 from the last and it is inclusive
# End position is 3 from the last and it is exclusive
print(s[-6:-3])

# String Reverse
print(s[::-1])