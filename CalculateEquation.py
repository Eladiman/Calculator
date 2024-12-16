from Stack import Stack
from Evaluator import evaluate
from Exceptions import *
from Arithmetic_unit import *
from Validation import *
from Parser import *


def calculate_equation(string: str):
    string = string.replace(" ", "")
    string = string.replace("   ", "")
    basic_expression_check(string)
    check_characters_validity(string)
    final_expression = combine_numbers_to_float(string)
    tilde_check(final_expression)
    parentheses_check(final_expression)
    right_unary_check(final_expression)
    final_expression = minus_parse(final_expression)
    final_expression = parse(final_expression)
    print(evaluate(final_expression))

