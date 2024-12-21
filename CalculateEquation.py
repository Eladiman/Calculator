from Evaluator import evaluate
from validation import *
from Parser import minus_parse, parse


def calculate_equation(string: str):
    string = "".join(string.split())
    check_characters_validity(string)
    basic_expression_check(string)
    final_expression = combine_numbers_to_float(string)
    tilde_check(final_expression)
    parentheses_check(final_expression)
    right_unary_check(final_expression)
    final_expression = minus_parse(final_expression)
    final_expression = parse(final_expression)

    result = evaluate(final_expression)
    try:
        result = float(result)
        if str(result) == "inf":
            raise OverflowError()
    except OverflowError:
        print("Math Error: The following number is too much big for this calculator.")
        raise OverflowError
    return result
