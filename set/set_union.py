skill1 = {'Java', 'c++'}
skill2 = {'Java', 'Javascript'}

combined_skill1 = skill1.union(skill2)
# alternative syntax
combined_skill2 = skill1 | skill2
print(combined_skill1)
print(combined_skill2)

# | accepts only two or multiple sets. union () accepts any kind of iterables

skill3 = {'dart'}

combined_skill3 = skill1.union(skill2).union(skill3)
print(combined_skill3)