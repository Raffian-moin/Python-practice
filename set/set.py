skills = {'python', 'c', 'C'}

print(skills)

# define empty set

sports = set()

if not sports :
    print('hello')

my_fav_movie = ['mad max', 'matrix']

# passing iterable to make a set
movies = set(my_fav_movie)

# order of the item has changed
print(movies)

my_word = set("mark my words")

# duplicate characters have been removed by default
print(my_word)

# getting size of set
print(len(my_word))

# check if an element is in set

if 'm' in my_word :
    print('found')

# alternative

if 'z' not in my_word :
    print('not found')


# add element to the set

movies.add('Highway')

print(movies)

# remove element from set

movies.remove('Highway')
print(movies)

# if we want to remove element that doesn't exist in set it throws error
# following will throw error as Highway 2 doesn't exist 
# movies.remove('Highway 2')

# to avoid error
movies.discard('Highway 2')

# remove and return an element

# it will randomly remove an element
removed_item = movies.pop()

print(removed_item)

# empty a set

movies.clear()
print(movies)

# to make a set immutable

skills = frozenset(skills)
# can't mutate the set
# following will throw error
# skills.add('ruby')

# loop through set

for skill in skills :
    print(skill)

# with index

for index, skill in enumerate(skills) :
    print(index, skill)

# by default index starts from 0, change the starting index
for index, skill in enumerate(skills, 10) :
    print(index, skill)
