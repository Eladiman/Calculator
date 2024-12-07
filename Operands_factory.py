from Arithmetic_unit import *


def Operands(operand):
    if operand == '+':
        return Add()
    elif operand == '-':
        return Decrease()
    elif operand == '/':
        return Divide()
    elif operand == '*':
        return Multiply()
    elif operand == '^':
        return Power()
    elif operand == '%':
        return Modulo()
    elif operand == '$':
        return Maximum()
    elif operand == '&':
        return Minimum()
    elif operand == '@':
        return Avg()
    elif operand == '~':
        return Tilde()
    elif operand == '!':
        return Factorial()
    else:
        #raise custom exception
        pass

