from Stack import Stack
from Evaluator import evaluate
from Exceptions import *
from Arithmetic_unit import *


def print_str(string):
    string.pop()
    str.__sizeof__()
    print(string)


if __name__ == '__main__':
    # print(float(5.2-5.3))
    #print(float(evaluate([5,5,'!','+'])))
    try:
        print(float(evaluate([0, 0, '^'])))
    except NotValidFactorialNumberError as e:
        print(e)
    except DivisionByZeroError as e:
        print(e)
    except NotValidPowerError as e:
        print(e)