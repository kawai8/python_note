# rsplit method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.rsplit

"""
[Syntax]
str.rsplit(sep=None, maxsplit=-1)

[Parameter]
sep: separator
maxsplit: the maximum number of splits

[Return]
a list of the words in the string, using sep as the delimiter string.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('Return a list of the words'.rsplit())
# output: ['Return', 'a', 'list', 'of', 'the', 'words']

print('Return a list of the words'.rsplit(maxsplit=3))
# output: ['Return a list', 'of', 'the', 'words']
