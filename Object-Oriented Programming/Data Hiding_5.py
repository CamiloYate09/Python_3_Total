'''
Data Hiding

A key part of object-oriented programming is encapsulation, which involves packaging of related variables and functions into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of a class should be hidden, and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here", meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no ways of enforcing a method or attribute be strictly private.
'''


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)