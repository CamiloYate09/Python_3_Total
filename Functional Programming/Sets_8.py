'''
Sets

Sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function. They share some functionality with lists, such as the use of in to check whether they contain a particular item.
'''

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

# /Example :2
letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2)

    # Example: 3

    nums = {1, 2, 1, 3, 1, 4, 5, 6}
    print(nums)
    nums.add(-7)
    nums.remove(3)
    print(nums)

# Example : 4
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
