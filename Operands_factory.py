"""
Module: operator_factory

This module provides a function to return the corresponding arithmetic operation object
based on a given character. The Operators include basic arithmetic operations,
such as addition, subtraction, multiplication, division, and more advanced operations
like factorial and digit sum. If an unrecognized operator is provided, an error is raised.

Functions:
    Operators(operator): Returns an operation object based on the operator character.
"""
from Arithmetic_unit import *
from Exceptions import UseOfAnWantedChar


def operators(operator):
    """
    Returns the corresponding operation object based on the operator character.

    Args:
        operator (str): A string representing an arithmetic operation. Supported operands:
                       '+', '-', '/', '*', '^', '%', '$', '&', '@', '~', '!', '#'.

    Returns:
        object: An instance of the corresponding operation class (e.g., Add, Decrease, Divide).

    Raises:
        UseOfAnWantedChar: If the operator is not a recognized operation character.

    Example:
        Operands('+')  : Returns an instance of the Add class.
    """
    if operator == '+':
        return Add()
    elif operator == '-':
        return Decrease()
    elif operator == '/':
        return Divide()
    elif operator == '*':
        return Multiply()
    elif operator == '^':
        return Power()
    elif operator == '%':
        return Modulo()
    elif operator == '$':
        return Maximum()
    elif operator == '&':
        return Minimum()
    elif operator == '@':
        return Avg()
    elif operator == '~':
        return Tilde()
    elif operator == '!':
        return Factorial()
    elif operator == '#':
        return DigitSum()
    else:
        raise UseOfAnWantedChar()


