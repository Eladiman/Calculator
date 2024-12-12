from Stack import *
from Evaluator import is_float
from Operands_factory import *
from Exceptions import *


def operator_grater(operator1, operator2):
    op1 = Operands(operator1)
    op2 = Operands(operator2)
    return op1.get_order() >= op2.get_order()


def check_characters_validity(string: str):
    index = 0
    while index != string.__len__():
        if not string[index].isdecimal() and not string[index] == '(' and not string[index] == ')' and not string[
                                                                                                               index] == '.':
            temp = Operands(string[index])
        index += 1


def combine_numbers(string: str):
    index = 0
    point_counter = 0
    res = []
    integer_res = []
    while index != string.__len__():
        if string[index].isdecimal() or string[index] == '.':
            if string[index] == '.':
                if integer_res.__len__() == 0 or point_counter == 1:
                    raise NotValidFloatError()
                else:
                    point_counter += 1
            integer_res.append(string[index])
        else:
            if integer_res.__len__() != 0:
                if integer_res[integer_res.__len__() - 1] == '.':
                    raise NotValidFloatError()
                temp = ''.join(integer_res)
                res.append(temp)
            res.append(string[index])
            integer_res = []
            point_counter = 0
        index += 1
    if integer_res.__len__() != 0:
        if integer_res[integer_res.__len__() - 1] == '.':
            raise NotValidFloatError()
        temp = ''.join(integer_res)
        res.append(temp)
    return res


def final_parse(string: str) -> list:
    string = string.replace(" ", "")
    string = string.replace("   ", "")
    check_characters_validity(string)
    final_string = combine_numbers(string)


def parse(string: list) -> list:
    str_post = []
    index = 0
    operand_stack = Stack()
    while not string.__len__() == 0:
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
