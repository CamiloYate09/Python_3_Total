'''
Generators

Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
They can be created using functions and the yield statement.
Example:
'''


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)


# # Example: 2
# Generators
#
# Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
# In fact, they can be infinite!


def infinite_sevens():
    while True:
        yield 7



for i in infinite_sevens():
    print(i)


# Example: 3

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))



# Example: 4

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))