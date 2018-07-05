'''
Tuple Unpacking

Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.
Example:
'''

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)



print('*************************************')

# Tuple Unpacking
#
# A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.
# Example:

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)




a, b, c, d, *e, f, g = range(20)
print(len(e))