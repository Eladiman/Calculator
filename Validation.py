from Operands_factory import *
from Evaluator import is_float
from Exceptions import *
from Stack import *


def check_characters_validity(string: str):
    index = 0
    while index != string.__len__():
        if not string[index].isdecimal() and not string[index] == '(' and not string[index] == ')' and not string[
                                                                                                               index] == '.':
            temp = Operands(string[index])
        index += 1


def basic_expression_check(string: str):
    if string.__len__() == 0:
        raise NotValidExpressionError("empty equation!")
    if not string[0].isdecimal() and string[0] != '(' and string[0] != '-' and string[0] != '~' and string[0] != '.':
        raise NotValidExpressionError(f"equation can't start with {string[0]} ")
    last_char = string[string.__len__() - 1]
    if not last_char.isdecimal() and last_char != ')' and last_char != '!' and last_char != '#':
        raise NotValidExpressionError(f"equation can't end with {last_char} ")


def tilde_check(expression: list):
    index = 0
    while index != expression.__len__():
        current_symb = expression[index]
        if current_symb == '~':
            if index != 0 and is_float(expression[index - 1]):
                raise NotValidTildeError("Attempted Unlawful Use of ~ : number before ~.")
            elif expression[index + 1] == '-':
                index += 1
                while index != expression.__len__() and not is_float(expression[index]) and expression[index] != '(':
                    if expression[index] != '-':
                        raise NotValidTildeError()
                    index += 1
            elif not is_float(expression[index + 1]) and expression[index + 1] != '(':
                raise NotValidTildeError(f"{expression[index + 1]} can't be after ~")

        index += 1


def parentheses_check(expression: list):
    openers_stack = Stack()
    index = 0
    while index != expression.__len__():
        if expression[index] == '(':
            if expression[index + 1] != '-' and expression[index + 1] != '~' and expression[
                index + 1] != '(' and not is_float(expression[index + 1]):
                raise NotValidParenthesesError(f"after ( can't come {expression[index + 1]}")
            openers_stack.push('(')
        elif expression[index] == ')':
            if openers_stack.is_empty():
                raise NotValidParenthesesError("There is ) without (")
            elif expression[index - 1] != '!' and expression[index - 1] != '#' and expression[
                index - 1] != ')' and not is_float(expression[index - 1]):
                raise NotValidParenthesesError(f"before ) can't come {expression[index - 1]}")
            openers_stack.pop()
        index += 1
    if not openers_stack.is_empty():
        raise NotValidParenthesesError("Error: There is an: ( without: )")


def combine_numbers_to_float(string: str):
    index = 0
    res = []
    integer_res = []
    while index != string.__len__():
        if string[index].isdecimal() or string[index] == '.':
            integer_res.append(string[index])
        else:
            if integer_res.__len__() != 0:
                temp = ''.join(integer_res)
                if not is_float(temp) or integer_res[integer_res.__len__() - 1] == '.':
                    raise NotValidFloatError()
                res.append(temp)
            res.append(string[index])
            integer_res = []
        index += 1
    if integer_res.__len__() != 0:
        temp = ''.join(integer_res)
        if not is_float(temp) or integer_res[integer_res.__len__() - 1] == '.':
            raise NotValidFloatError()
        res.append(temp)
    return res
