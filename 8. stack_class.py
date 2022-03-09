"""
Write a Program in Python to implement a Stack Data Structure using
Class and Objects, with push, pop, and traversal method.
"""
"""
implementation of stack using list in python
By 20CE155 ADNAN VAHORA
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


if __name__ == '__main__':
    s = Stack()  # Create the stack object
    print(s.is_empty())  # True
    s.push(4)  # Push 4 to the stack
    s.push('dog')  # Push dog to the stack
    s.push(True)  # Push True to the stack
    print(s.items)  # Prints [4, 'dog', True]
    print(s.pop())  # Prints True
    print(s.items)  # Prints [4, 'dog']
