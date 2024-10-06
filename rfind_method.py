# rfind method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.rfind

"""
[Syntax]
str.rfind(sub[, start[, end]])

[Parameter]
sub: the substring to search for 
start: start index
end: end index

[Return]
the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. 
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('0123456789'.rfind('3'))
# output: 3

print('01234567893'.rfind('3'))
# output : 10

print('01234567893'.rfind('3', 1, 10))
# output : 3

#print('01234567893'.rfind('a', 1, 10))
# output : -1
