# rstrip method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.rstrip

"""
[Syntax]
str.rstrip([chars])

[Parameter]
chars: a string specifying the set of characters to be removed.  

[Return]
a copy of the string with trailing characters removed
"""

# ------------------------------------------
# Example
# ------------------------------------------
print("'" + '   spacious   '.rstrip() + "'")
# output: '   spacious'

print("'" + 'mississippi'.rstrip('ipzi') + "'")
# output: 'mississ'
