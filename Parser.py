from Stack import *
from Evaluator import is_float
from Operands_factory import *
from Exceptions import *
from Validation import *
from Arithmetic_unit import UnaryMinus


def operator_grater(operator1, operator2):
    if operator1 == '(' or operator2 == '(':
        return False
    op1 = Operands(operator1)
    op2 = Operands(operator2)
    return op1.get_order() >= op2.get_order()


def final_parse(string: str) -> list:
    string = string.replace(" ", "")
    string = string.replace("   ", "")
    check_characters_validity(string)


def minus_parse(string: list):
    index = 0
    while not index == len(string):
        if string[index] == '-':
            if index == 0 or string[index - 1] == '(':
                while string[index] == '-':
                    string[index] = 'UM'
                    index += 1
                if string[index] != '(' and not is_float(string[index]):
                    raise NotValidMinusError(f"Error! Attempted of use {string[index]} after Unary Minus")
            elif string[index - 1] == ')' or is_float(string[index-1]) or (isinstance(Operands(string[index - 1]), Unary) and not Operands(string[index - 1]).is_left()):
                    string[index] = 'D'
                    index += 1
                    while string[index] == '-':
                        string[index] = 'SM'
                        index += 1
                    if string[index] != '(' and not is_float(string[index]):
                        raise NotValidMinusError(f"Error! Attempted of use {string[index]} after -")
            else:
                while string[index] == '-':
                    string[index] = 'SM'
                    index += 1
                if string[index] != '(' and not is_float(string[index]):
                    raise NotValidMinusError(f"Error! Attempted of use {string[index]} after -")
        else:
            index += 1
    return string


def parse(string: list) -> list:
    str_post = []
    index = 0
    operand_stack = Stack()
    while not len(string) == 0:
        symb = string.pop(0)
        if is_float(symb):
            str_post.append(symb)
        else:
            if symb == ')':
                while not operand_stack.is_empty() and not operand_stack.top() == '(':
                    str_post.append(operand_stack.pop())
                operand_stack.pop()
            else:
                while not operand_stack.is_empty() and operator_grater(operand_stack.top(), symb):
                    str_post.append(operand_stack.pop())
                operand_stack.push(symb)
    while not operand_stack.is_empty():
        str_post.append(operand_stack.pop())
    return str_post
