# rpartition method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.rpartition

"""
[Syntax]
str.rpartition(sep)

[Parameter]
sep: separator 

[Return]
a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('example@xxx.come'.rpartition('@'))
# output: ('example', '@', 'xxx.come')

print('example@xxx.come@zzzz'.rpartition('@'))
# output: ('example@xxx.come', '@', 'zzzz')
