# rindex method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.rindex

"""
[Syntax]
str.rindex(sub[, start[, end]])

[Parameter]
sub: the substring to search for
start: start index
end: end index

[Return]
the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. 
Like rfind() but raises ValueError when the substring sub is not found.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('0123456789'.rindex('3'))
# output: 3

print('01234567893'.rindex('3'))
# output : 10

print('01234567893'.rindex('3', 1, 10))
# output : 3

#print('01234567893'.rindex('a', 1, 10))
# output : ValueError: substring not found
