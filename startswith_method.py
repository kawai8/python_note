# startswith method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.startswith

"""
[Syntax]
str.startswith(prefix[, start[, end]])

[Parameter]
prefix: string or tuple
start: start position
end: end position

[Return]
True if string starts with the prefix
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('python programmer'.startswith('py'))
# output: True

print('python programmer'.startswith('thon', 2, 8))
# output: True
