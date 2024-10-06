# splitlines method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.splitlines

"""
[Syntax]
str.splitlines(keepends=False)

[Parameter]
keepends: whether line breaks are included in the result

[Return]
a list of the lines in the string, breaking at line boundaries. 
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('ab c\n\nde fg\rkl\r\n'.splitlines())
# output: ['ab c', '', 'de fg', 'kl']

print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))
# output: ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
