# format method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.format
# https://docs.python.org/3/library/string.html#format-examples

"""
[Syntax]
str.format(*args, **kwargs)

[Parameter]
args: positional arguments
kwargs: keyword arguments

[Return]
the formatted string.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
# output: c, b, a

print('{:,}'.format(1234567890))
# output: 1,234,567,890

print('{:<30}'.format('left aligned'))
# output: left aligned

print('{:>30}'.format('right aligned'))
# output:                  right aligned

print('{:*^30}'.format('centered'))
# output: ***********centered***********

print('{:.2%}'.format(19/22))
# output: 86.36%

import datetime
d = datetime.datetime(2020, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
# output: 2020-07-04 12:15:58
