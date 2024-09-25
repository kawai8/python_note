# index method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.index

"""
[Syntax]
str.index(sub[, start[, end]])

[Parameter]
sub: substring
start: starting position
end: ending position

[Return]
the lowest index in the string where substring sub is found within the slice s[start:end].
ValueError when the substring is not found.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('abcdabcdabcd'.index('a', 2, 8))
# output: 4
