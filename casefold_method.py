# casefold method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.casefold

"""
[Syntax]
str.casefold()

[Parameter]
none 

[Return]
a casefolded copy of the string
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('Super Programmer'.casefold())
# output: uper programmer

# Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. 
print('ß'.casefold())
# output: ss
print('ß'.lower())
# output: ß
