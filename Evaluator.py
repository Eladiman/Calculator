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
        if not isinstance(temp, Operator) and is_float(temp):
            result.push(temp)
        else:
            operator = temp
            if isinstance(operator, Unary):
                if not is_float(result.top()):
                    raise NotValidExpressionError(f"after{operator} can't come {type(result.top()).__name__}.")
                first_operand = float(result.pop())
                try:
                    value = operator.calculate([first_operand])
                    if value != value or str(value) == "inf":
                        raise OverflowError()
                except OverflowError:
                    print(
                        f"{first_operand} and {type(operator).__name__} creates a very big number that can't be calculated!")
                    raise OverflowError()
                result.push(value)
            else:
                if not is_float(result.top()):
                    raise NotValidExpressionError(f"after{type(operator).__name__} can't come {type(result.top()).__name__}.")
                second_operand = float(result.pop())
                if result.is_empty():
                    raise NotValidExpressionError(f"There is a Missing Operand! please enter another equation")
                if not is_float(result.top()):
                    raise NotValidExpressionError(f"after{type(operator).__name__} can't come {type(result.top()).__name__}.")
                first_operand = float(result.pop())
                try:
                    value = operator.calculate([first_operand, second_operand])
                    if value != value or str(value) == "inf":
                        raise OverflowError()
                except OverflowError:
                    print(
                        f"{first_operand, type(operator).__name__, second_operand} creates a very big number that can't be calculated!")
                    raise OverflowError()
                result.push(value)
    last = result.pop()
    if not result.is_empty():
        raise NotValidExpressionError("Equation not solvable! there is a missing operator")
    return last
