from Stack import Stack
from Operands_factory import *


def is_digit(x):
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)


def is_float(element: any) -> bool:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def evaluate(string: list):
    result = Stack()
    while not string.__len__() == 0:
        temp = string.pop(0)
        if is_float(temp):
            result.push(temp)
        else:
            operator = Operands(temp)
            if operator.is_unary():
                first_operand = float(result.pop())
                value = operator.calculate([first_operand])
                result.push(value)
            else:
                second_operand = float(result.pop())
                first_operand = float(result.pop())
                value = operator.calculate([first_operand, second_operand])
                result.push(value)
    last = result.pop()
    if not result.is_empty():
        raise NotValidExpressionError("Equation not solvable! there is a missing operator")
    return last
