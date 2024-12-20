import pytest
from CalculateEquation import calculate_equation
from Exceptions import *

EPSILON = 0.1


def test_division_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        calculate_equation("(3*4)/0")


def test_not_valid_factorial_error():
    with pytest.raises(NotValidFactorialNumberError):
        calculate_equation("2--3!")


def test_not_valid_power_error():
    with pytest.raises(NotValidPowerError):
        calculate_equation("(-2)^1.5")


def test_not_valid_char_error():
    with pytest.raises(UseOfAnWantedChar):
        calculate_equation("(3*4)+A-2")


def test_not_valid_modulo_error():
    with pytest.raises(NotValidModuloError):
        calculate_equation("(3*4) % 0")


def test_missed_float_use_error():
    with pytest.raises(NotValidFloatError):
        calculate_equation("3.22.3 + 4")


def test_missed_parentheses_use_error():
    with pytest.raises(NotValidParenthesesError):
        calculate_equation("((3+2))) - 4")


def test_missed_tilde_use_error():
    with pytest.raises(NotValidTildeError):
        calculate_equation("~ --- ~ 2")


def test_missed_unary_minus_use_error():
    with pytest.raises(NotValidMinusError):
        calculate_equation("---~2")


def test_missed_sign_minus_use_error():
    with pytest.raises(NotValidMinusError):
        calculate_equation("2+---+3")


def test_missed_binary_minus_use_error():
    with pytest.raises(NotValidMinusError):
        calculate_equation("2-+3")


def test_missed_digit_sum_use_error():
    with pytest.raises(NotValidDigitSumError):
        calculate_equation("(-3.3)#")


def test_missed_right_unary_operator_use_error():
    with pytest.raises(NotValidRightUnaryError):
        calculate_equation("2+!3")


def test_empty_equation_error():
    with pytest.raises(NotValidExpressionError):
        calculate_equation("")


def test_expression_error1():
    with pytest.raises(NotValidExpressionError):
        calculate_equation("3^*2")


def test_expression_error2():
    with pytest.raises(NotValidExpressionError):
        calculate_equation("3(3)")


def test_expression_error3():
    with pytest.raises(NotValidExpressionError):
        calculate_equation("9!~2")


def test_expression_error4():
    with pytest.raises(NotValidExpressionError):
        calculate_equation("9!(2)")


def test_white_spaces_equation():
    assert calculate_equation("     2                   +3 ") == 5


def test_simple_plus_equation():
    assert calculate_equation("3+3") == 6


def test_simple_decrease_equation():
    assert calculate_equation("123-23") == 100


def test_simple_multiply_equation():
    assert calculate_equation("25*8") == 200


def test_simple_divide_equation():
    assert calculate_equation("200/4") == 50


def test_simple_power_equation():
    assert calculate_equation("2^3") == 8


def test_simple_modulo_equation():
    assert calculate_equation("22%3") == 1


def test_simple_max_equation():
    assert calculate_equation("5$9") == 9


def test_simple_min_equation():
    assert calculate_equation("5&9") == 5


def test_simple_avg_equation():
    assert calculate_equation("10@2") == 6


def test_simple_tilde_equation():
    assert calculate_equation("~2+6") == 4


def test_simple_factorial_equation():
    assert calculate_equation("5!-2") == 118


def test_simple_digit_sum_equation():
    assert calculate_equation("2.2222222#") == 16


def test_simple_unary_minus_equation():
    assert calculate_equation("---3!") == -6


def test_simple_sign_minus_equation():
    assert calculate_equation("2+--3!") == 8


def test_complex_equation1():
    assert calculate_equation("(7 + 3) * 5! - 10 @ ((6$2)#) ^ (1^2) * 8&9 * (2.5)") == 1040


def test_complex_equation2():
    assert calculate_equation("(9 * 3) + 2! @ 8 & 4 ^ 5 $ (3 * 2) + 8 + 1.23") == 4132.23


def test_complex_equation3():
    assert calculate_equation("(2 * 3) - 4--- 3@ ~6 & (8 ^ 4) $ (7 - 1.23) + 2 + ~ 10") == -11.77


def test_complex_equation4():
    assert calculate_equation("-----3! - ~2 ^ (2 - 4) $ (8+-2) ----- 10 * 2! + 9 # ") == -81


def test_complex_equation5():
    assert calculate_equation("(~5 @ 7) $ ((15 & 8)# ! + 4^2) % (3! * (~2 $ 6))") == 16


def test_complex_equation6():
    assert calculate_equation("~(15# ^ 2) @ ((42# $ 7) & (~3 * 4!))") == -54


def test_complex_equation7():
    assert calculate_equation("(25# * 3!) @ (16# $ (8# & 7^2))") == 45.5


def test_complex_equation8():
    assert abs(calculate_equation("~(15 @ 9) * (27# $ 8) + ((4 & 7) ^ (3!)) / (3.25 * (12 @ 4))") - 49.54) < EPSILON


def test_complex_equation9():
    assert calculate_equation("((12.5 @ 7.5) & ~4) ^ (31# $ (5 * 2)) + (15 & 9) * ((21# @ 6) $ 12)") == 1048684


def test_complex_equation10():
    assert calculate_equation("(~((16 $ 7)#) @ 12) * ((25# & 8) ^ 3) + (9.75 & 15) * ((18 @ 6) $ 3!)") == 974.5


def test_complex_equation11():
    assert calculate_equation("( (2 * 2) + 3 ) ^ 2 @ 4 + (9! #) - 7 % 2") == 369


def test_complex_equation12():
    assert calculate_equation("--2 @ 3 * (5! - 2) + 3 ^ ~4 & (6 - 1.5) $ 8 # + 2!") == 6858


def test_complex_equation13():
    assert calculate_equation("(7 * 4) @ ~5 + 3! & 2 ^ 9 $ (8 - 1) # * 6") == 3083.5


def test_complex_equation14():
    assert calculate_equation("(3 ^ 3) * ~6 @ 5! $ (7 - 3) + 2.2222# ") == 1549


def test_complex_equation15():
    assert calculate_equation("2+-2 ^ 3 * 2! @ ~6 + 7 & (4 - 1) $ 2  ") == 21


def test_complex_equation16():
    assert calculate_equation("2 ^ (3 & 1) * (8 + ~4) $ 6! @ 2 & (10 - 1.5) # -(5 ^ 3) + 4!") == -75


def test_complex_equation17():
    assert calculate_equation("((5! * (3 + 2)) @ (9 * ~4)) + ((7 - 1) * (8 + 2)) $ ((6 - 2) * 5) & 3 - (4! + 2)") == 259


def test_complex_equation18():
    assert calculate_equation("4! * 2 ^ 3 @ ~7 $ 6 + 8 * 2 & 10.11111# +-----4 - 1") == 1547


def test_complex_equation19():
    assert calculate_equation("---9 * --(3! + 5) ## @ 7 - ~2 $ 8 & 4 - (6 - 1)") == -49.5


def test_complex_equation20():
    assert calculate_equation("-3+2 @ (2 ^ 2) + 5 * 5! - 4! $ (8 & 2) + 2 ^ ~4 * (2! + 10) @ 8 # + -2^3") == 568.625
