from Exceptions import *


class Operator:

    def calculate(self, operands):
        raise NotImplementedError()

    def is_unary(self):
        raise NotImplementedError()


class Add(Operator):
    ORDER = 1

    def calculate(self, operands):
        return operands[0] + operands[1]

    def is_unary(self):
        return False


class Decrease(Operator):
    ORDER = 1

    #minus onary
    def calculate(self, operands):
        return operands[0] - operands[1]

    def is_unary(self):
        return False


class Divide(Operator):
    ORDER = 2

    def calculate(self, operands):
        if operands[1] == 0:
            raise DivisionByZeroError("Division by zero Error! please try to insert another equation")
        return operands[0] / operands[1]

    def is_unary(self):
        return False


class Multiply(Operator):
    ORDER = 2

    def calculate(self, operands):
        return operands[0] * operands[1]

    def is_unary(self):
        return False


class Power(Operator):
    ORDER = 3

    def calculate(self, operands):
        if operands[0] == operands[1] == 0:
            raise NotValidPowerError("Attempted Unlawful Use of Power! please try to insert another equation ")
        return operands[0] ** operands[1]

    def is_unary(self):
        return False


class Modulo(Operator):
    #to do
    pass


class Maximum(Operator):
    ORDER = 4

    def calculate(self, operands):
        return max(operands)

    def is_unary(self):
        return False


class Minimum(Operator):
    ORDER = 4

    def calculate(self, operands):
        return min(operands)

    def is_unary(self):
        return False


class Avg(Operator):
    ORDER = 5

    def calculate(self, operands):
        return (operands[0] + operands[1]) / 2

    def is_unary(self):
        return False


class Tilde(Operator):
    ORDER = 6

    def calculate(self, operands):
        return - operands[0]

    def is_unary(self):
        return True


class Factorial(Operator):
    ORDER = 6

    def calculate(self, operands):
        if operands[0] < 0 or isinstance(operands[0], float) :
            raise NotValidFactorialNumberError("Attempted Unlawful Use of Factorial! please try to insert another equation ")
        result = 1
        for index in range(2, operands[0] + 1):
            result *= index
        return result

    def is_unary(self):
        return True
