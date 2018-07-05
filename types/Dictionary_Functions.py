'''
Dictionary Functions
Just like lists, dictionary keys can be assigned to different values.
However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
'''
squares = {1: 1, 2: 3, 3: "error", 4: 15}

squares[8] = 64
squares[3] = 9
print(squares)


#Example:2
primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])


# Example: 3

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


# Example: 4

pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))


# Example: 5

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))