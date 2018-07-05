'''
filter

The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
Example:
'''

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)