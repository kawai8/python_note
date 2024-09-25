# find method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.find

"""
[Syntax]
str.find(sub[, start[, end]])

[Parameter]
sub: substring
start: starting index
end: ending index

[Return]
the lowest index in the string where substring sub is found within the slice s[start:end].
-1 if sub is not found.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('abcdabcdabcd'.find('a', 2, 8))
# output: 4
