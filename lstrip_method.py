# lstrip method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.lstrip

"""
[Syntax]
str.lstrip([chars])

[Parameter]
chars: a string specifying the set of characters to be removed. 

[Return]
a copy of the string with leading characters removed.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print("'" + '  spacious   '.lstrip() + "'")
# output: 'spacious   '

print("'" + 'www.example.com'.lstrip('cmowz.') + "'")
# output: 'example.com'
