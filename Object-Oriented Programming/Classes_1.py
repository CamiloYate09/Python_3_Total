'''
Classes

We have previously looked at two paradigms of programming - imperative (using statements, loops, and functions as subroutines), and functional (using pure functions, higher-order functions, and recursion).

Another very popular paradigm is object-oriented programming (OOP).
Objects are created using classes, which are actually the focal point of OOP.
The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the keyword class and an indented block, which contains class methods (which are functions).
Below is an example of a simple class and its objects.
'''

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
print(felix.color, felix.legs)
print(rover.color, rover.legs)
print(stumpy.color, stumpy.legs)

#
# __init__
#
# The __init__ method is the most important method in a class.
# This is called when an instance (object) of the class is created, using the class name as a function.
#
# All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self argument to the list for you; you do not need to include it when you call the methods. Within a method definition, self refers to the instance calling the method.
#
# Instances of a class have attributes, which are pieces of data associated with them.
# In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.
# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
# Example:

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)


# # Example 3
# Methods
#
# Classes can have other methods defined to add functionality to them.
# Remember, that all methods must have self as their first parameter.
# These methods are accessed using the same dot syntax as attributes.
# Example:


class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()


# Example 3
# Trying to access an attribute of an instance that isn't defined causes an AttributeError. This also applies when you call an undefined method.

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

rect = Rectangle(7, 8)
print(rect.color)