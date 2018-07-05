'''
Function Arguments

Python allows to have function with varying number of arguments.
Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.
Example:
'''

def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)



print('******************************************************')

# Default Values
#
# Named parameters to a function can be made optional by giving them a default value.
# These must come after named parameters without a default value.
# Example:

def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")



print('***********************************************')

# Function Arguments
#
# **kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
# Example:

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

