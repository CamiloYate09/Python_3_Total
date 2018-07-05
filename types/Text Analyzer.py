'''
Text Analyzer

This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
This section shows how a file could be open and read.
'''

filename = input("prueba_Text_Analyzer.txt")

with open(filename) as f:
    text = f.read()

print(text)



# Example: 2
#
# Text Analyzer
#
# This part of the program shows a function that counts how many times a character occurs in a string.

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

# Leer el archivo

filename = input("prueba_Text_Analyzer")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))

