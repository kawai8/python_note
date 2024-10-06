# split method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.split

"""
[Syntax]
str.split(sep=None, maxsplit=-1)

[Parameter]
sep: separetor
maxsplit: the maximum number of splits

[Return]
a list of the words in the string, using sep as the delimiter string. 
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('1,2,3'.split(','))
# output: ['1', '2', '3']

print('1,2,3'.split(',', maxsplit=1))
# output: ['1', '2,3']
