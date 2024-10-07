# strip method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.strip

"""
[Syntax]
str.strip(chars])

[Parameter]
chars: a string specifying the set of characters to be removed

If omitted or None, the chars argument defaults to removing whitespace. 
# import string
# string.whitespace

[Return]
a copy of the string with the leading and trailing characters removed
"""

# ------------------------------------------
# Example
# ------------------------------------------
print("'" + '  spacious   '.strip() + "'")
# output: 'spacious'

print("'" + 'www.example.com'.strip('cmowz.') + "'")
# output: 'example'
