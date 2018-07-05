'''
Metacharacters

Some more metacharacters are *, +, ?, { and }.
These specify numbers of repetitions.
The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses.
Example:
'''

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")


print('************************************************')

# Metacharacters
#
# The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".
# Example:

import re

pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")


print('***********************************************')
# Example 3

# Metacharacters
#
# The metacharacter ? means "zero or one repetitions".
# Example:

import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")