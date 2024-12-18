from CalculateEquation import calculate_equation
from Exceptions import *
from Validation import combine_numbers_to_float
from Parser import *


def print_str(string):
    string.pop()
    str.__sizeof__()
    print(string)


if __name__ == '__main__':
    end = False
    while not end:
        try:
            expression = input("Please Enter your equation. write STOP to finish : ")
            if expression.upper() == "STOP":
                end = True
            else:
                calculate_equation(expression)
                #print(combine_numbers_to_float(expression))
                #print(parse((combine_numbers_to_float(expression))))
        except NotValidFactorialNumberError as e:
            print(e)
        except DivisionByZeroError as e:
            print(e)
        except NotValidPowerError as e:
            print(e)
        except NotValidFloatError as e:
            print(e)
        except UseOfAnWantedChar as e:
            print(e)
        except NotValidParenthesesError as e:
            print(e)
        except NotValidMinusError as e:
            print(e)
        except NotValidExpressionError as e:
            print(e)
        except NotValidTildeError as e:
            print(e)
        except NotValidModuloError as e:
            print(e)
        except NotValidDigitSumError as e:
            print(e)
        except NotValidRightUnaryError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except KeyboardInterrupt as e:
            print(e)
        except OverflowError:
            pass

