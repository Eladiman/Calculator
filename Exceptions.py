class DivisionByZeroError(Exception):
    def __init__(self, message="Division by zero Error! please try to insert another equation"):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class NotValidFactorialNumberError(Exception):
    def __init__(self, message="Attempted Unlawful Use of Factorial! please try to insert another equation "):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class NotValidPowerError(Exception):
    def __init__(self, message="Attempted Unlawful Use of Power! please try to insert another equation "):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UseOfAnWantedChar(Exception):
    def __init__(self,
                 message="There is a letter or a non operator char in your equasion! please try to insert another equation "):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class NotValidModuloError(Exception):
    def __init__(self, message="Attempted Unlawful Use of modulo! please try to insert another equation "):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class NotValidFloatError(Exception):
    def __init__(self, message="Attempted Unlawful Use of . ! please try to insert another equation "):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
