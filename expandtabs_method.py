# expandtabs method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.expandtabs

"""
[Syntax]
str.expandtabs(tabsize=8)

[Parameter]
tabsize: A number specifying the tabsize 

[Return]
a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('01\t012\t0123\t01234'.expandtabs(4))
# output: 01  012 0123    01234
