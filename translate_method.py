# translate method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.translate

"""
[Syntax]
str.translate(table)

[Parameter]
table: a translation table 

[Return]
a copy of the string in which each character has been mapped through the given translation table
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('engin engin engin'.translate(str.maketrans("eng", "ENG")))
# output: ENGiN ENGiN ENGiN
