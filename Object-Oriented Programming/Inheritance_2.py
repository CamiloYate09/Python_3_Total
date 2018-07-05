'''
Inheritance

Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name).
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
To inherit a class from another class, put the superclass name in parentheses after the class name.
Example:
'''


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()



# # Example 2:
# Inheritance
#
# A class that inherits from another class is called a subclass.
# A class that is inherited from is called a superclass.
# If a class inherits from another with the same attributes or methods, it overrides them.


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof")


husky = Dog("Max", "grey")
husky.bark()


# # Exmaple 3:
#
# Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.
# Example:


class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()