# join method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.join

"""
[Syntax]
str.join(iterable)

[Parameter]
iterable: iterable object
          list, tuple, string, dictionary, set

[Return]
a string which is the concatenation of the strings in iterable.
"""

# ------------------------------------------
# Example
# ------------------------------------------
mytup = (1, 'two', 3)
print(','.join(map(str, mytup)))
# output: 1,two,3

mydic = {'a':'111', 'b':'222', 'c':'333'}
print(','.join(mydic))
# 'a,b,c'

print(','.join(mydic.values()))
# 111,222,333'
