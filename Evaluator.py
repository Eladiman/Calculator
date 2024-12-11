from Stack import Stack
from Operands_factory import *


def is_digit(x):
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)


def evaluate(string: list):
    result = Stack()
    while not string.__len__() == 0:
        temp = string.pop(0)
        if is_digit(temp):
            result.push(temp)
        else:
            operator = Operands(temp)
            if operator.is_unary():
                first_operand = result.pop()
                value = operator.calculate([first_operand])
                result.push(value)
            else:
                second_operand = result.pop()
                first_operand = result.pop()
                value = operator.calculate([first_operand, second_operand])
                result.push(value)
    return result.pop()
