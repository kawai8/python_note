# removeprefix method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.removeprefix
# Added in version 3.9.

"""
[Syntax]
str.removeprefix(prefix, /)

[Parameter]
prefix: prefix string

[Return]
string[len(prefix):]
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('TestHook'.removeprefix('Test'))
print('TestHook'[len('Test'):])
# output: Hook

print('BaseTestHook'.removeprefix('Test'))
# output: BaseTestHook
