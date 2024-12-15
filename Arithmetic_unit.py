from Exceptions import *


class Operator:

    def calculate(self, operands):
        raise NotImplementedError()

    def get_order(self):
        raise NotImplementedError()


class Binary(Operator):
    pass


class Unary(Operator):
    def is_left(self):
        raise NotImplementedError()


class Add(Binary):
    ORDER = 1

    def calculate(self, operands):
        return operands[0] + operands[1]

    def get_order(self):
        return 1


class Decrease(Binary):
    ORDER = 1

    #minus onary
    def calculate(self, operands):
        return operands[0] - operands[1]

    def get_order(self):
        return 1


class Divide(Binary):
    ORDER = 2

    def calculate(self, operands):
        if operands[1] == 0:
            raise DivisionByZeroError()
        return operands[0] / operands[1]

    def get_order(self):
        return 2


class Multiply(Binary):
    ORDER = 2

    def calculate(self, operands):
        return operands[0] * operands[1]

    def get_order(self):
        return 2


class UnaryMinus(Unary):
    ORDER = 2.5

    def calculate(self, operands):
        return - operands[0]

    def get_order(self):
        return 2.5

    def is_left(self):
        return True


class Power(Binary):
    ORDER = 3

    def calculate(self, operands):
        if operands[0] == operands[1] == 0:
            raise NotValidPowerError("Error : Can't Solve 0^0.")
        if operands[0] < 0 and not operands[1].is_integer():
            raise NotValidPowerError("Error : Attempted of sqrt to a negative number.")
        return operands[0] ** operands[1]

    def get_order(self):
        return 3


class Modulo(Binary):
    ORDER = 3

    def calculate(self, operands):
        if operands[1] == 0:
            raise NotValidModuloError(f"Attempted Unlawful Use of modulo! can't solve {operands[0]} % {operands[1]}")
        return operands[0] % operands[1]

    def get_order(self):
        return 3


class Maximum(Binary):
    ORDER = 4

    def calculate(self, operands):
        return max(operands)

    def get_order(self):
        return 4


class Minimum(Binary):
    ORDER = 4

    def calculate(self, operands):
        return min(operands)

    def get_order(self):
        return 4


class Avg(Binary):
    ORDER = 5

    def calculate(self, operands):
        return (operands[0] + operands[1]) / 2

    def get_order(self):
        return 5


class Tilde(Unary):
    ORDER = 6

    def calculate(self, operands):
        return - operands[0]

    def is_left(self):
        return True

    def get_order(self):
        return 6


class Factorial(Unary):
    ORDER = 6

    def calculate(self, operands):
        check_num = operands[0]
        if operands[0] < 0 or not check_num.is_integer():
            raise NotValidFactorialNumberError()
        result = 1.0
        num = int(operands[0])
        if num > 170:
            raise OverflowError()
        for index in range(2, num + 1):
            result *= index
        return result

    def is_left(self):
        return False

    def get_order(self):
        return 6


class SignMinus(Unary):
    ORDER = 69

    def calculate(self, operands):
        return - operands[0]

    def is_left(self):
        return True

    def get_order(self):
        return 10
