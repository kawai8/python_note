# replace method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.replace

"""
[Syntax]
str.replace(old, new[, count])

[Parameter]
old: the substring to search for
new: the substring to replace the old with
count: the number of times to replace the old　with the new

[Return]
a copy of the string with all occurrences of substring old replaced by new.
"""

# ------------------------------------------
# Example
# ------------------------------------------
print('python programmer'.replace("python", "C"))
# output: C programmer

print('foo foo foo bar foo bar bar'.replace("foo", "run", 2))
# output: run run foo bar foo bar bar
