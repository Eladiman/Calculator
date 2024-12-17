from Stack import *
from Evaluator import is_float
from Operands_factory import *
from Exceptions import *
from Validation import *
from Arithmetic_unit import UnaryMinus, Decrease, SignMinus


def operator_grater(operator1, operator2):
    if not isinstance(operator1, Operator) or (
            isinstance(operator1, UnaryMinus) and isinstance(operator2, UnaryMinus)) \
            or (isinstance(operator1, SignMinus) and isinstance(operator2, SignMinus)):  # in case of operator1 is (
        return False
    return operator1.get_order() >= operator2.get_order()


def minus_parse(string: list):
    index = 0
    while not index == len(string):
        if string[index] == '-':
            if index == 0 or string[index - 1] == '(':
                while string[index] == '-':
                    string[index] = UnaryMinus()
                    index += 1
                if string[index] != '(' and not is_float(string[index]):
                    raise NotValidMinusError(f"Error! Attempted of use {string[index]} after Unary Minus")
            elif string[index - 1] == ')' or is_float(string[index - 1]) or (
                    isinstance(Operands(string[index - 1]), Unary) and not Operands(string[index - 1]).is_left()):
                string[index] = Decrease()
                index += 1
                while string[index] == '-':
                    string[index] = SignMinus()
                    index += 1
                if string[index] != '(' and not is_float(string[index]) and (
                        isinstance(string[index - 1], Decrease) and string[index] != '~'):
                    raise NotValidMinusError(f"Error! Attempted of use {string[index]} after -")
                elif string[index] != '(' and not is_float(string[index]) and not isinstance(string[index - 1], Decrease):
                    raise NotValidMinusError(f"Error! Attempted of use {string[index]} after SignMinus")
            else:
                while string[index] == '-':
                    string[index] = SignMinus()
                    index += 1
                if string[index] != '(' and not is_float(string[index]):
                    raise NotValidMinusError(f"Error! Attempted of use {string[index]} after SignMinus")
        else:
            index += 1
    return string


def parse(string: list) -> list:
    str_post = []
    operator_stack = Stack()
    while not len(string) == 0:
        symb = string.pop(0)
        if not isinstance(symb, Operator) and is_float(symb):
            str_post.append(symb)
        else:
            if not isinstance(symb, Operator) and symb == ')':
                while not operator_stack.is_empty() and isinstance(operator_stack.top(), Operator):
                    str_post.append(operator_stack.pop())
                operator_stack.pop()
            elif not isinstance(symb, Operator) and symb == '(':
                operator_stack.push(symb)
            else:
                operator = symb
                if not isinstance(symb, Operator):
                    operator = Operands(symb)
                while not operator_stack.is_empty() and operator_grater(operator_stack.top(), operator):
                    str_post.append(operator_stack.pop())
                operator_stack.push(operator)
    while not operator_stack.is_empty():
        str_post.append(operator_stack.pop())
    return str_post
