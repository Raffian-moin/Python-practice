language1 = {'c', 'python'}
language2 = {'c', 'html'}
language3 = {'css', 'php'}

language_union = language1.union(language2).union(language3)
print(language_union)

language_union2 = language1 | language2
print(language_union2)

# set() vs pipe(|) operator

# set accepts sets, lists, dictionary and converts them in set and then does the union
# but pipe only accepts set