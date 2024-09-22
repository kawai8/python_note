# New in version 3.6.
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# formatted string literal

name = "Fred"
print(f"He said his name is {name!r}.")
# He said his name is 'Fred'.

foo = "bar"
print(f"{ foo = }")
#  foo = 'bar'

from datetime import datetime
today = datetime(year=2022, month=1, day=3)
print(f"{today:%B %d, %Y}")
# January 03, 2022
print(f"{today=:%B %d, %Y}")
# today=January 03, 2022

now = datetime.now()
print(f"{now:%Y}/{now:%m}/{now:%d} {now:%H}:{now:%M}:{now:%S}")
# 2023/09/23 01:37:13
