# encode method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.encode

"""
[Syntax]
str.encode(encoding='utf-8', errors='strict')

[Parameter]
encoding: the encoding type
errors: errors controls
        https://docs.python.org/3/library/codecs.html#error-handlers

[Return]
the string encoded to bytes.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('日本語'.encode(encoding='utf-8'))
# output: b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'
