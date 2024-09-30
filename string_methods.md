# [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
| No. | Method            | Description | Example |
| --: | ----------------- | ----------- | ----------- |
|1| [capitalize()](https://docs.python.org/3/library/stdtypes.html#str.capitalize)   | Return a copy of the string with its first character capitalized. | [code](https://github.com/kawai8/python_note/blob/main/capitalize_method.py) |
|2| [casefold()](https://docs.python.org/3/library/stdtypes.html#str.casefold) | Return a casefolded copy of the string. | [code](https://github.com/kawai8/python_note/blob/main/casefold_method.py) |
|3| [center()](https://docs.python.org/3/library/stdtypes.html#str.center) | Return centered in a string of length width. | [code](https://github.com/kawai8/python_note/blob/main/center_method.py) |
|4| [count()](https://docs.python.org/3/library/stdtypes.html#str.count) | Return the number of non-overlapping occurrences of substring sub in the range [start, end]. | [code](https://github.com/kawai8/python_note/blob/main/count_method.py) |
|5| [encode()](https://docs.python.org/3/library/stdtypes.html#str.encode) | Return the string encoded to bytes. | [code](https://github.com/kawai8/python_note/blob/main/encode_method.py) |
|6| [endswith()](https://docs.python.org/3/library/stdtypes.html#str.endswith) | Return True if the string ends with the specified suffix, otherwise return False. | [code](https://github.com/kawai8/python_note/blob/main/endswith_method.py) |
|7| [expandtabs()](https://docs.python.org/3/library/stdtypes.html#str.expandtabs) | Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. | [code](https://github.com/kawai8/python_note/blob/main/expandtabs_method.py) |
|8| [find()](https://docs.python.org/3/library/stdtypes.html#str.find) | Return the lowest index in the string where substring sub is found within the slice s[start:end]. Return -1 if sub is not found.  | [code](https://github.com/kawai8/python_note/blob/main/find_method.py) |
|9| [format()](https://docs.python.org/3/library/stdtypes.html#str.format) | Perform a string formatting operation. | [code](https://github.com/kawai8/python_note/blob/main/format_method.py) |
|10| [format_map()](https://docs.python.org/3/library/stdtypes.html#str.format_map) | Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. | [code](https://github.com/kawai8/python_note/blob/main/format_map_method.py) |
|11| [index()](https://docs.python.org/3/library/stdtypes.html#str.index) | Like find(), but raise ValueError when the substring is not found. | [code](https://github.com/kawai8/python_note/blob/main/index_method.py) |
|12| [isalnum()](https://docs.python.org/3/library/stdtypes.html#str.isalnum)   | Return True if all characters in the string are alphanumeric |
|13| [isalpha()](https://docs.python.org/3/library/stdtypes.html#str.isalpha)     | Return True if all characters in the string are alphabetic  |
|14| [isascii()](https://docs.python.org/3/library/stdtypes.html#str.isascii)     | Return True if the string is empty or all characters in the string are ASCII |
|15| [isdecimal()](https://docs.python.org/3/library/stdtypes.html#str.isdecimal)   | Return True if all characters in the string are decimal characters |
|16| [isdigit()](https://docs.python.org/3/library/stdtypes.html#str.isdigit)     | Return True if all characters in the string are digits |
|17| [isidentifier()](https://docs.python.org/3/library/stdtypes.html#str.isidentifier)| Return True if the string is a valid identifier according to the language definition |
|18| [islower()](https://docs.python.org/3/library/stdtypes.html#str.islower)     | Return True if all cased characters in the string are lowercase |
|19| [isnumeric()](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)   | Return True if all characters in the string are numeric characters |
|20| [isprintable()](https://docs.python.org/3/library/stdtypes.html#str.isprintable) | Return True if all characters in the string are printable or the string is empty |
|21| [isspace()](https://docs.python.org/3/library/stdtypes.html#str.isspace)     | Return True if there are only whitespace characters in the string |
|22| [istitle()](https://docs.python.org/3/library/stdtypes.html#str.istitle)     | Return True if the string is a titlecased string |
|23| [isupper()](https://docs.python.org/3/library/stdtypes.html#str.isupper)     | Return True if all cased characters in the string are uppercase |
|24| [join()](https://docs.python.org/3/library/stdtypes.html#str.join) | Return a string which is the concatenation of the strings in iterable. | [code](https://github.com/kawai8/python_note/blob/main/join_method.py) |
|25| [ljust()](https://docs.python.org/3/library/stdtypes.html#str.ljust) | Return the string left justified in a string of length width. | [code](https://github.com/kawai8/python_note/blob/main/ljust_method.py) |
|26| [lower()](https://docs.python.org/3/library/stdtypes.html#str.lower) | Return a copy of the string with all the cased characters converted to lowercase. | [code](https://github.com/kawai8/python_note/blob/main/lower_method.py) |
|27| [lstrip()](https://docs.python.org/3/library/stdtypes.html#str.lstrip) | Return a copy of the string with leading characters removed. | [code](https://github.com/kawai8/python_note/blob/main/lstrip_method.py) |
|28| [maketrans()](https://docs.python.org/3/library/stdtypes.html#str.maketrans) |  |  |
|29| [partition()](https://docs.python.org/3/library/stdtypes.html#str.partition) |  |  |
|30| [removeprefix()](https://docs.python.org/3/library/stdtypes.html#str.removeprefix) |  |  |
|31| [removesuffix()](https://docs.python.org/3/library/stdtypes.html#str.removesuffix) |  |  |
|32| [replace()](https://docs.python.org/3/library/stdtypes.html#str.replace) |  |  |
|33| [rfind()](https://docs.python.org/3/library/stdtypes.html#str.rfind) |  |  |
|34| [rindex()](https://docs.python.org/3/library/stdtypes.html#str.rindex) |  |  |
|35| [rjust()](https://docs.python.org/3/library/stdtypes.html#str.rjust) |  |  |
|36| [rpartition()](https://docs.python.org/3/library/stdtypes.html#str.rpartition) |  |  |
|37| [rsplit()](https://docs.python.org/3/library/stdtypes.html#str.rsplit) |  |  |
|38| [rstrip](https://docs.python.org/3/library/stdtypes.html#str.rstrip) |  |  |
|39| [split()](https://docs.python.org/3/library/stdtypes.html#str.split) |  |  |
|40| [splitlines()](https://docs.python.org/3/library/stdtypes.html#str.splitlines) |  |  |
|41| [startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith) |  |  |
|42| [strip()](https://docs.python.org/3/library/stdtypes.html#str.strip) |  |  |
|43| [swapcase()](https://docs.python.org/3/library/stdtypes.html#str.swapcase) |  |  |
|44| [title()](https://docs.python.org/3/library/stdtypes.html#str.title) |  |  |
|45| [translate()](https://docs.python.org/3/library/stdtypes.html#str.translate) |  |  |
|46| [upper()](https://docs.python.org/3/library/stdtypes.html#str.upper) |  |  |
|47| [zfill()](https://docs.python.org/3/library/stdtypes.html#str.zfill) |  |  |
