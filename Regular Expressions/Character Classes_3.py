'''
Character Classes

Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.
Example:
'''

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")



print('**********************************************************')
#
# Character Classes
#
# Character classes can also match ranges of characters.
# Some examples:
# The class [a-z] matches any lowercase alphabetic character.
# The class [G-P] matches any uppercase character from G to P.
# The class [0-9] matches any digit.
# Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
# Example:


import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")