# class str
# https://docs.python.org/3/library/stdtypes.html#string-methods


## upper method
'python'.upper()
# 'PYTHON'
'ｐｙｔｈｏｎ'.upper() # two-byte character
# 'ＰＹＴＨＯＮ'


# lower method
'PYTHON'.lower()
# 'python'
'ＰＹＴＨＯＮ'.lower() # two-byte character
# 'ｐｙｔｈｏｎ'


# swapcase method
'Hello Python'.swapcase()
# 'hELLO pYTHON'


# capitalize method
'python programmer'.capitalize()
# 'Python programmer'


# title method
'python programmer'.title()
# 'Python Programmer'


# replace method
# str.replace(old, new[, count])
'python programmer'.replace("python", "C")
# 'C programmer'
'foo foo foo bar foo bar bar'.replace("foo", "run", 2)
# 'run run foo bar foo bar bar'


# translate method
# str.translate(table)
'engin engin engin'.translate(str.maketrans("eng", "ENG"))
#'ENGiN ENGiN ENGiN'

