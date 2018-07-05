'''
String Formatting

So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
String formatting provides a more powerful way to embed non-strings within strings. String formatting uses a string's format method to substitute a number of arguments in the string.

'''

# Example: 1

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

# Example: 2
print("{0}{1}{0}".format("abra", "cad"))



#Example: 3

a = "{x}, {y}".format(x=5, y=12)
print(a)


