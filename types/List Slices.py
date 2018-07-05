'''
List Slices

List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.
'''

# Example:1
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])


# Example:2
# '''
# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.
# '''
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])


# Example: 3
# List Slices
#
# List slices can also have a third number, representing the step, to include only alternate values in the slice.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])


# Example: 4

# List Slices
#
# Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
