# https://docs.python.org/3/library/stdtypes.html#dict.setdefault
# setdefault(key[, default])

my_dict = {1: 'dog', 2: 'cat'}
my_dict.setdefault(3, 'bird')
print(my_dict)
# {1: 'dog', 2: 'cat', 3: 'bird'}




for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
print(by_letter)
# {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

#----------------------------------------------
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
#----------------------------------------------
