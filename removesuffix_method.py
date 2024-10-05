# removesuffix method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.removesuffix
# Added in version 3.9.

"""
[Syntax]
str.removesuffix(suffix, /)

[Parameter]
suffix: suffix string

[Return]
string[:-len(suffix)]
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('MiscTest'.removesuffix('Test'))
print('MiscTest'[:-len('Test'):])
# output: Misc

print('TmpDirMixin'.removesuffix('Test'))
# output: TmpDirMixin
