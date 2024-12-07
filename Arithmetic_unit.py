class Operator:

    def calculate(self, operands):
        raise NotImplementedError()


class Add(Operator):
    ORDER = 1

    def calculate(self, operands):
        return operands[0] + operands[1]


class Decrease(Operator):
    ORDER = 1

    #minus onary
    def calculate(self, operands):
        return operands[0] - operands[1]


class Divide(Operator):
    ORDER = 2

    #exception divide by zero
    def calculate(self, operands):
        return operands[0] / operands[1]


class Multiply(Operator):
    ORDER = 2

    def calculate(self, operands):
        return operands[0] * operands[1]


class Power(Operator):
    ORDER = 3

    #to do - 0^0 is 1
    def calculate(self, operands):
        return operands[0] ** operands[1]


class Modulo(Operator):
    #to do
    pass


class Maximum(Operator):
    ORDER = 4

    def calculate(self, operands):
        return max(operands)


class Minimum(Operator):
    ORDER = 4

    def calculate(self, operands):
        return min(operands)


class Avg(Operator):
    ORDER = 5

    def calculate(self, operands):
        return (operands[0] + operands[1]) / 2


class Tilde(Operator):
    ORDER = 6

    def calculate(self, operands):
        return - operands[0]


class Factorial(Operator):
    ORDER = 6

    #to do - exceptions not integer, smaler then 0
    def calculate(self, operands):
        result = 1
        for index in range(2, operands[0]):
            result *= index
        return result
