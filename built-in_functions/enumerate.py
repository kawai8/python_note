# enumerate(iterable, start=0)

my_list = ['cat', 'dog', 'bird']
for i, animal in enumerate(my_list, start=1)
    print(i, animal)
# 1 cat
# 2 dog
# 3 bird


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]


