# Indexing
str1 = 'python'
print(str1[0])
# p


# Note that since -0 is the same as 0, negative indices start from -1.
print(str1[-1]) # last character
print(str1[len(str1) -1]) 
# n



# Attempting to use an index that is too large will result in an error
print(str1[10])
# Traceback (most recent call last):
#   File "006.py", line 33, in <module>
#     print(str1[10])
# IndexError: string index out of range
