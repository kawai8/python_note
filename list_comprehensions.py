# https://docs.python.org/3.9/tutorial/datastructures.html#list-comprehensions
'''
[expression for variable in iterable]
[expression for variable in iterable if condition]
'''

# for loop
listA = []
for i in range(10):
   listA.append(i**2)
print(listA)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# List Comprehensions
listB = [i**2 for i in range(10)]
print(listB)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Filtering
odd_list = [i**2 for i in range(10) if i % 2 == 1]  # Add only odd numbers
print(odd_list)
# [1, 9, 25, 49, 81]


# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
nested_list = [[row[i] for row in matrix] for i in range(4)]
print(nested_list)


# dictionary
dicA = {i: i**2 for i in range(5)}
print(dicA)

# set
setA = {i**2%10 for i in range(10)}
print(setA)

# generator expression
g = (i**2 for i in range(5))
for num in g:
    print(num)
