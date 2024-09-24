# endswith method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.endswith

"""
[Syntax]
str.endswith(suffix[, start[, end]])

[Parameter]
suffix: string or tuple of suffixes
start: beginning position
end: ending position

[Return]
True if the string ends with the specified suffix.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('python programmer'.endswith('mmer'))
# output: True  

print('suffix can also be a tuple of suffixes to look for.'.endswith(('for.', 'can')))
# output: True  
