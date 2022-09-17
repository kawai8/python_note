# Slicing
'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''



str1 = 'python'
print(str1[2:5])
# tho

# an omitted first index defaults to zero
print(str1[:2])
# py

# an omitted second index defaults to the size of the string being sliced.
print(str1[4:])
print(str1[-2:])
# on

# [start:stop:step]
print(str1[0:4:2])
# pt



# Note how the start is always included, and the end always excluded.
print(str1[:2] + str1[2:])
# python

# out of range slice indexes are handled gracefully when used for slicing:
print(str1[0:10])
# python

