'''
Metacharacters

Metacharacters are what make regular expressions more powerful than normal string methods.
They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a literal metacharacter, such as "$". You can do this by escaping the metacharacters by putting a backslash in front of them.
However, this can cause problems, since backslashes also have an escaping function in normal Python strings. This can mean putting three or four backslashes in a row to do all the escaping.
'''

# Metacharacters
#
# The first metacharacter we will look at is . (dot).
# This matches any character, other than a new line.
# Example:

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")


print('***********************************************************')
#
# Metacharacters
#
# The next two metacharacters are ^ and $.
# These match the start and end of a string, respectively.
# Example:

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")


print('*******************************************************')

# Curly Braces
#
# Curly braces can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something".
# Hence {0,1} is the same thing as ?.
# If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
# Example:


import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")