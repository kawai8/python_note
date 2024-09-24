# count method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.count

"""
[Syntax]
str.count(sub[, start[, end]])

[Parameter]
sub: substring 
start: starting index
end: ending index

[Return]
the number of non-overlapping occurrences of substring sub in the range [start, end].
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('cat cat dog cat dog'.count('cat'))
# output: 3

print('Cat cAt dog cat dog'.count('cat'))
# output: 1

print('Cat cAt dog cat dog'.lower().count('cat'))
# output: 3
