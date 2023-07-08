# General Formula
# collection[start:stop:step]

s='abcdefghijklmnopqrstupwxyz'

# Get every characters positioned in odd
print(s[::2])

# Get every characters positioned in even
print(s[1::2])

# Here we omit start and end position and say that step is 1 thus return as whole string
print(s[::1])

# So while reversing we omit start and end position and say that step is negative -1 thus
# returning us while string in reverse order
print(s[::-1])