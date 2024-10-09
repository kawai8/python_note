# zfill method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.zfill

"""
[Syntax]
str.zfill(width)

[Parameter]
width: the length of the returned string

[Return]
a copy of the string left filled with ASCII '0' digits to make a string of length width
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('42'.zfill(5))
# output: 00042

print('-42'.zfill(5))
# output: -0042

print('text'.zfill(5))
# output: 0text
