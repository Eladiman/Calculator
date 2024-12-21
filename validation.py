"""
Module: validation

This module contains various functions used for validating and processing mathematical expressions.
The functions check for the validity of several rules.
It includes checks for:
    - Valid characters in the expression
    - Expression structure (starting and ending characters) or empty expression
    - Valid usage right unary operators
    - Proper use of parentheses
    - Combining numbers into floats - if the number is valid to convert to float
    - Special rules for tilde (~) usage
"""
from Operands_factory import *
from Evaluator import is_float
from Exceptions import *
from stack import *


def check_characters_validity(string: str):
    """
    Validates that each character in the string is a valid character for a mathematical expression.
    the string has to contain only the following characters: (1234567890!@#$%^&*~-+()./)

    Args:
        string (str): The string representing the expression to validate.

    Raises:
        UseofAnWantedChar: If any character in the string is not a :
        -operand,
        -operator,
        -decimal point.
        -parentheses
    """
    index = 0
    while index != string.__len__():
        if (not string[index].isdecimal() and not string[index] == '('
                and not string[index] == ')' and not string[index] == '.'):
            # check if can be converted to operator. raise exception if can't
            operators(string[index])
        index += 1


def basic_expression_check(string: str):
    """
    Checks if the basic structure of the expression is valid, including:
    - Empty strings
    - Invalid starting characters. expression can't start with:
        -non (left unary operators) such as: ! or +
        -closing parentheses : )
    - Invalid ending characters expression can't end with:
        -non (right unary operators) such as: ~ or +
        -opening parentheses : (
        -a dot: 3. is not valid

    Args:
        string (str): The string representing the expression to check.

    Raises:
        NotValidExpressionError: If the expression is:
            - empty,
            - starts or ends with an invalid character.
    """
    if string.__len__() == 0:
        raise NotValidExpressionError("empty equation!")
    if (not string[0].isdecimal() and string[0] != '(' and string[0] != '-' and
            string[0] != '~' and string[0] != '.'):
        raise NotValidExpressionError(f"equation can't start with {string[0]} ")
    last_char = string[string.__len__() - 1]
    if not last_char.isdecimal() and last_char != ')' and last_char != '!' and last_char != '#':
        raise NotValidExpressionError(f"equation can't end with {last_char} ")


def right_unary_check(expression: list):
    """
    Checks for valid usage of right unary operators in the expression. Specifically,
    verifies that no operator is placed before a right unary operator.

    Args:
        expression (list): The expression to validate as a list of operands and operators.

    Raises:
        NotValidRightUnaryError: If an invalid right unary operator is found.
    """
    index = 0
    while index != len(expression):
        if (not is_float(expression[index]) and expression[index] != '(' and
                expression[index] != ')'):
            operator = operators(expression[index])
            # check if the char is right unary operator and the char before him is not number
            if (isinstance(operator, Unary) and not operator.is_left() and
                    not is_float(expression[index - 1])):
                if expression[index - 1] != '(' and expression[index - 1] != ')':
                    # check if the operator before is right unary. if not raise an exception
                    before_operator = operators(expression[index - 1])
                    if not (isinstance(before_operator, Unary) and not operator.is_left()):
                        raise NotValidRightUnaryError(f"before {expression[index]} can't come "
                                                      f"{expression[index - 1]}")
        index += 1


def tilde_check(expression: list):
    """
    Validates the correct usage of the tilde (~) operator in the expression.
    it checks if the following rules for tilde are fulfill:
    - a tilde can't be placed after operand
    - the tilde must be followed by a :
        -number,
        -opening parenthesis,
        -a signMinus(-) that belong to the expression to his right.
    - tilde can come twice in a row:
        ~~2 is not valid
        ~------~2- is not valid.

    Args:
        expression (list): The expression to validate as a list of operands and operators.

    Raises:
        NotValidTildeError: If the tilde operator is used unlawfully.
    """
    index = 0
    while index != expression.__len__():
        current_symb = expression[index]
        if current_symb == '~':
            # check the first rule
            if index != 0 and is_float(expression[index - 1]):
                raise NotValidTildeError("Attempted Unlawful Use of ~ : number before ~.")
            elif expression[index + 1] == '-':
                # check the second and third rule
                index += 1
                while (index != expression.__len__() and not is_float(expression[index]) and
                       expression[index] != '('):
                    if expression[index] != '-':
                        raise NotValidTildeError()
                    index += 1
            # check the second rule
            elif not is_float(expression[index + 1]) and expression[index + 1] != '(':
                raise NotValidTildeError(f"Attempted Unlawful Use of ~ :"
                                         f" {expression[index + 1]} can't be after ~")

        index += 1


def parentheses_check(expression: list):
    """
    Checks if the parentheses in the expression are balanced and used correctly. Specifically:
    - Ensures that every opening parenthesis has a corresponding closing parenthesis.
    - Validates the usage of characters immediately before and after parentheses.
        after opening parentheses can come only:
            - operand
            -opening parentheses
            -left unary operators
        before closing parentheses can come only:
            - operand
            -closing parentheses
            -right unary operators

    Args:
        expression (list): The expression to validate as a list of operands and operators.

    Raises:
        NotValidParenthesesError: If the parentheses are not balanced or used incorrectly.
    """
    openers_stack = Stack()
    index = 0
    while index != expression.__len__():
        if expression[index] == '(':
            if (expression[index + 1] != '-' and expression[index + 1] != '~' and
                    expression[index + 1] != '(' and not is_float(expression[index + 1])):
                raise NotValidParenthesesError(f"Attempted Unlawful Use of parentheses! :"
                                               f" after ( can't come {expression[index + 1]}")
            openers_stack.push('(')
        elif expression[index] == ')':
            # check if there are opening without closers
            if openers_stack.is_empty():
                raise NotValidParenthesesError("Attempted Unlawful Use of parentheses! :"
                                               " There is an: ( without: )")

            elif (expression[index - 1] != '!' and expression[index - 1] != '#' and
                  expression[index - 1] != ')' and not is_float(expression[index - 1])):
                raise NotValidParenthesesError(
                    f"Attempted Unlawful Use of parentheses! : "
                    f"before ) can't come {expression[index - 1]}")
            openers_stack.pop()
        index += 1
    # check if there are opening without closers
    if not openers_stack.is_empty():
        raise NotValidParenthesesError("Attempted Unlawful Use of parentheses! :"
                                       " There is an: ( without: )")


def combine_numbers_to_float(string: str):
    """
    The following function goes through a string.
    if it finds a set of consecutive numbers, it groups them into one number.
        -example: the string "123+48" will be converted to: ["123","+","48"]
    The function also validates that the number is a valid float.
    and does not end with a decimal point.

    Args:
        string (str): The string representing the equation.

    Returns:
        list: A list that represents the equation but the following numbers are grouped into one.
        example: the string "123+48" will be converted to: ["123","+","48"]

    Raises:
        NotValidFloatError: If the string cannot be converted into a valid float.
    """
    index = 0
    res = []
    integer_res = []  # the combine number
    while index != string.__len__():
        if string[index].isdecimal() or string[index] == '.':
            integer_res.append(string[index])
        else:
            if integer_res.__len__() != 0:
                # if the list that represents the combine number is not empty.
                # we check that it is a legal number using the method is_float
                # and if it is a float then it shouldn't end with a dot.
                temp = ''.join(integer_res)
                if not is_float(temp) or integer_res[integer_res.__len__() - 1] == '.':
                    raise NotValidFloatError()
                res.append(temp)
            res.append(string[index])
            integer_res = []
        index += 1
    # check if there was a number at the end of the string. if so add it to list
    if integer_res.__len__() != 0:
        temp = ''.join(integer_res)
        if not is_float(temp) or integer_res[integer_res.__len__() - 1] == '.':
            raise NotValidFloatError()
        res.append(temp)
    return res
