from Stack import Stack
from Evaluator import evaluate
from Exceptions import *
from Arithmetic_unit import *
from Parser import *


def print_str(string):
    string.pop()
    str.__sizeof__()
    print(string)


if __name__ == '__main__':
    # print(float(5.2-5.3))
    #print(float(evaluate([5,5,'!','+'])))
    try:
        str = combine_numbers("3.3")
        index = 0
        while index != str.__len__():
            print(str[index])
            index += 1
        check_characters_validity("1")
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