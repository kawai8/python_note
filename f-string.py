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


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# %Y year(yyyy)
# %y year(yy)
# %m month
# %d day of month(01-31)
# %H hour(00-23)
# %I hour(00-12)
# %M minute(00-59)
# %S second(00-59)
# %f microsecond(000000-999999)
# %z UTC offset
# %Z timezone name
# %p AM/PM
# %a weekday short
# %A weekday full
# %b month name short
# %B month name full
