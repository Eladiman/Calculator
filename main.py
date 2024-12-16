from CalculateEquation import calculate_equation
from Exceptions import *


def print_str(string):
    string.pop()
    str.__sizeof__()
    print(string)


if __name__ == '__main__':
    end = False
    while not end:
        try:
            expression = input("Please Enter your equation. write STOP to finish : ")
            if expression == "STOP":
                end = True
            else:
                calculate_equation(expression)
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
        except OverflowError:
            pass

