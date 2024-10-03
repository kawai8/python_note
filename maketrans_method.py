# maketrans method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.maketrans

"""
[Syntax]
str.maketrans(x[, y[, z]])

[Parameter]
x:
If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None. Character keys will then be converted to ordinals.
y:
If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. 
z:
If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
[Return]
a translation table usable for translate method.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('engin engin engin'.translate(str.maketrans("eng", "ENG")))
# output: ENGiN ENGiN ENGiN
