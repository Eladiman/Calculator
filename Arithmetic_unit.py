from Exceptions import *


class Operator:

    def calculate(self, operands):
        raise NotImplementedError()

    def is_unary(self):
        raise NotImplementedError()

    def get_order(self):
        raise NotImplementedError()


class Add(Operator):
    ORDER = 1

    def calculate(self, operands):
        return operands[0] + operands[1]

    def is_unary(self):
        return False

    def get_order(self):
        return 1


class Decrease(Operator):
    ORDER = 1

    #minus onary
    def calculate(self, operands):
        return operands[0] - operands[1]

    def is_unary(self):
        return False

    def get_order(self):
        return 1


class Divide(Operator):
    ORDER = 2

    def calculate(self, operands):
        if operands[1] == 0:
            raise DivisionByZeroError()
        return operands[0] / operands[1]

    def is_unary(self):
        return False

    def get_order(self):
        return 2


class Multiply(Operator):
    ORDER = 2

    def calculate(self, operands):
        return operands[0] * operands[1]

    def is_unary(self):
        return False

    def get_order(self):
        return 2


class Power(Operator):
    ORDER = 3

    def calculate(self, operands):
        if operands[0] == operands[1] == 0:
            raise NotValidPowerError()
        return operands[0] ** operands[1]

    def is_unary(self):
        return False

    def get_order(self):
        return 3


class Modulo(Operator):
    ORDER = 3

    def calculate(self, operands):
        if operands[1] == 0:
            raise NotValidModuloError()
        return operands[0] % operands[1]

    def is_unary(self):
        return False

    def get_order(self):
        return 3


class Maximum(Operator):
    ORDER = 4

    def calculate(self, operands):
        return max(operands)

    def is_unary(self):
        return False

    def get_order(self):
        return 4


class Minimum(Operator):
    ORDER = 4

    def calculate(self, operands):
        return min(operands)

    def is_unary(self):
        return False

    def get_order(self):
        return 4


class Avg(Operator):
    ORDER = 5

    def calculate(self, operands):
        return (operands[0] + operands[1]) / 2

    def is_unary(self):
        return False

    def get_order(self):
        return 5


class Tilde(Operator):
    ORDER = 6

    def calculate(self, operands):
        return - operands[0]

    def is_unary(self):
        return True

    def get_order(self):
        return 6


class Factorial(Operator):
    ORDER = 6

    def calculate(self, operands):
        check_num = operands[0]
        if operands[0] < 0 or not check_num.is_integer():
            raise NotValidFactorialNumberError()
        result = 1
        num = int(operands[0])
        for index in range(2, num + 1):
            result *= index
        return result

    def is_unary(self):
        return True

    def get_order(self):
        return 6
