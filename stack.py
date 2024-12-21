"""
Module: stack

This module contains the implementation of a simple stack data structure
using a list. The stack allows the following operations:
    - push: Add an element to the top of the stack.
    - pop: Remove and return the top element of the stack.
    - top: Peek at the top element without removing it.
    - is_empty: Check if the stack is empty.
    - to_string: Get a list representation of the stack.

Usage:
    stack1 = Stack()  # Create a new stack
    stack1.push(10)  # Push an element
    stack1.push(20)
    print(stack1.top())  # Output: 20 (top of the stack)
    stack1.pop()  # Remove top element
    print(stack1.is_empty())  # Output: False (stack is not empty)
    print(stack1.to_string())  # Output: the following list [10]
"""


class Stack:
    """
    A simple implementation of a stack data structure using a list.

    Attributes:
        _top_element (int): Index of the top element in the stack.
        _list (list): The underlying list holding the stack elements.

    Methods:
        __init__(self):
            Initializes the stack with an empty list and sets the top element index to -1.

        push(value):
            Adds an element to the top of the stack.

        top():
            Returns the element at the top of the stack without removing it.
            Returns None if the stack is empty.

        pop():
            Removes and returns the element at the top of the stack.
            Returns None if the stack is empty.

        is_empty():
            Checks if the stack is empty.

        to_string():
            Returns the list representation of the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack with _top_element set to -1 and an empty list.
        """
        self._top_element = -1
        self._list = []

    def push(self, value):
        """
        Adds an element to the top of the stack.

        Args:
            value: The value to be added to the stack.
        """
        self._top_element += 1
        self._list.insert(0, value)

    def top(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self._list[0]
        else:
            return None

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
            The element at the top of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            self._top_element -= 1
            temp = self._list[0]
            self._list.pop(0)
            return temp
        else:
            return None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self._top_element == -1

    def to_string(self):
        """
        Returns the list representation of the stack.

        Returns:
            list: The underlying list representing the stack.
        """
        return self._list
