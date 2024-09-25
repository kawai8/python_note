# format_map method
# str class
# https://docs.python.org/3/library/stdtypes.html#str.format_map

"""
[Syntax]
str.format_map(mapping)

[Parameter]
mapping: dictionary 

[Return]
the formatted string.
"""

# ------------------------------------------
# Example
# ------------------------------------------
mydic = {'name':'Tom', 'country':'japan'}
print('{name} was born in {country}'.format_map(mydic))
# output: tom was born in japan

class Default(dict):
    def __missing__(self, key):
        return key
print('{name} was born in {country}'.format_map(Default(name='Ken')))
# output: Ken was born in country
