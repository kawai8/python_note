# https://docs.python.org/3/library/functions.html#len


## string
len('hello world')
# 11
len('こんにちわ')
# 5

## bytes
len('鳥') 
# 1
len('鳥'.encode('utf-8'))
# 3
len('鳥'.encode('sjis'))
# 2

## tuple
len((0, 1, 2, 3, 4)) 
# 5

## list
len(['a', 'b', 'c'])
# 3

## range
len(range(7))
# 7

## dictionary
len({'key1':'val1', 'key2':'val2'})
# 2

## set
len({1, 2, 3, 4, 'a', 'b'})
# 6

## frozen set
len(frozenset({1, 'a'}))
# 2
