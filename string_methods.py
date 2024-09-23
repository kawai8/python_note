# class str
# https://docs.python.org/3/library/stdtypes.html#string-methods


##  capitalize method
##  str.capitalize()
'python programmer'.capitalize()
# 'Python programmer'


## casefole method
## str.casefold()
example
# 


## cetner method
## str.center(width[, fillchar])
example
# 


## count method
## str.count(sub[, start[, end]])
'cat cat dog cat dog'.count('cat')
# 3


## encode method
## str.encode(encoding='utf-8', errors='strict')
example
# output


## endswith method
## str.endswith(suffix[, start[, end]])
example
# output


## expandtabs method
## str.expandtabs(tabsize=8)
example
# output


## find method
## str.find(sub[, start[, end]])
'abcdabcdabcd'.find('a', 2, 8)
# 4


## format method
## str.format(*args, **kwargs)
## https://docs.python.org/3/library/string.html#format-examples

'{0}, {1}, {2}'.format('a', 'b', 'c')
# 'a, b, c'

'{:,}'.format(1234567890)
# '1,234,567,890'

# [d] Decimal Number
# [x] Hexadecimal Number
# [o] Octal Number
# [b] Binary Number
"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
# 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
# '+3.140000; -3.140000'
'{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
' 3.140000; -3.140000'
'{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
'3.140000; -3.140000

# Aligning the text and specifying a width
'{:<30}'.format('left aligned')
# 'left aligned 
'{:>30}'.format('right aligned')
# '                 right aligned'
'{:^30}'.format('centered')
# '           centered           '
'{:*^30}'.format('centered')
'***********centered***********'

# Accessing arguments by name
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)
# 'Coordinates: 37.24N, -115.81W'

'Correct answers: {:.2%}'.format(19/22)
# 'Correct answers: 86.36%'

import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(d)
# '2010-07-04 12:15:58'


## format_map method
## str.format_map(mapping)
example
# output


## index method
## str.index(sub[, start[, end]])
'abcdabcdabcd'.index('a', 2, 8)
# 4


## join method
##str.join(iterable)
mydic = {'a':'111', 'b':'222', 'c':'333'}
','.join(mydic)
# 'a,b,c'
','.join(mydic.values())
# 111,222,333'

mytup = (1, 'two', 3)
','.join(map(str, mytup))
# '1,two,3'


## ljust method
## str.ljust(width[, fillchar])
example
# output


## lower method
## str.lower()
'PYTHON'.lower()
# 'python'
'ＰＹＴＨＯＮ'.lower() # two-byte character
# 'ｐｙｔｈｏｎ'


## lstrip method
## str.lstrip([chars])
'   spacious   '.lstrip()
# 'spacious   '


## maketrans method
## static str.maketrans(x[, y[, z]])
example
# output


## partition method
## str.partition(sep)
example
# output


## removeprefix method
## str.removeprefix(prefix, /)
example
# output


## removesuffix method
## str.removesuffix(suffix, /)
example
# output


## replace method
## str.replace(old, new[, count])
'python programmer'.replace("python", "C")
# 'C programmer'
'foo foo foo bar foo bar bar'.replace("foo", "run", 2)
# 'run run foo bar foo bar bar'


## rfind method
## str.rfind(sub[, start[, end]])
'abcdabcdabcd'.rfind('a', 2, 10)
# 8


## rindex method
## str.rindex(sub[, start[, end]])
'abcdabcdabcd'.rindex('a', 2, 10)
# 8


## rjust method
## str.rjust(width[, fillchar])
example
# output


## rpartition method
## str.rpartition(sep)
example
# output


## rsplit method
## str.rsplit(sep=None, maxsplit=- 1)
example
# output


## rstrip method
## str.rstrip([chars])
'   spacious   '.rstrip()
# '   spacious'


## split method
## str.split(sep=None, maxsplit=-1)
'1,2,3'.split(',')
# ['1', '2', '3']


## splitlines method
## str.splitlines(keepends=False)
example
# output


## startswith method
## str.startswith(prefix[, start[, end]])
example
# output


## strip method
## str.strip([chars])
'   spacious   '.strip()
# 'spacious'
'#....... Section 3.2.1 Issue #32 .......'.strip('.#! ')
# 'Section 3.2.1 Issue #32'


## swapcase method
## str.swapcase()
'Hello Python'.swapcase()
# 'hELLO pYTHON'


## title method
## str.title()
'python programmer'.title()
# 'Python Programmer'


## translate method
## str.translate(table)
'engin engin engin'.translate(str.maketrans("eng", "ENG"))
#'ENGiN ENGiN ENGiN'


## upper method
## str.upper()
'python'.upper()
# 'PYTHON'
'ｐｙｔｈｏｎ'.upper() # two-byte character
# 'ＰＹＴＨＯＮ'


## zfill method
## str.zfill(width)
example
# output

