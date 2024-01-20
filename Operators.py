from math import pow


class Operator(object):
    def __init__(self, priority):
        self.priority = priority


class LeftOperator(Operator):
    def __init__(self, priority):
        super().__init__(priority)


class RightOperator(Operator):
    def __init__(self, priority):
        super().__init__(priority)


class BinaryOperator(Operator):
    def __init__(self, priority):
        super().__init__(priority)


# +
class Addition(BinaryOperator):
    def __init__(self):
        super().__init__(1)

    @staticmethod
    def calc(x1, x2):
        return x1+x2


# -
class Subtraction(BinaryOperator):
    def __init__(self):
        super().__init__(1)

    @staticmethod
    def calc(x1, x2):
        return x1-x2


# *
class Multiple(BinaryOperator):
    def __init__(self):
        super().__init__(2)

    @staticmethod
    def calc(x1, x2):
        return x1 * x2


# /
class Divide(BinaryOperator):
    def __init__(self):
        super().__init__(2)

    @staticmethod
    def calc(x1, x2):
        try:
            return x1 / x2
        except ZeroDivisionError as er:
            print("You can't divide by zero.")


# -
class MinusUnary(LeftOperator):
    def __init__(self):
        super().__init__(2.5)

    @staticmethod
    def calc(x1):
        return -x1


# ^
class Power(BinaryOperator):
    def __init__(self):
        super().__init__(3)

    @staticmethod
    def calc(x1, x2):
        return pow(x1, x2)


# %
class Module(BinaryOperator):
    def __init__(self):
        super().__init__(4)

    @staticmethod
    def calc(x1, x2):
        return x1 % x2


# @
class Average(BinaryOperator):
    def __init__(self):
        super().__init__(5)

    @staticmethod
    def calc(x1, x2):
        return (x1 + x2)/2


# $
class Maximum(BinaryOperator):
    def __init__(self):
        super().__init__(5)

    @staticmethod
    def calc(x1, x2):
        return max(x1, x2)


# &
class Minimum(BinaryOperator):
    def __init__(self):
        super().__init__(5)

    @staticmethod
    def calc(x1, x2):
        return min(x1, x2)


# !
class Factorial(RightOperator):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def calc(x1):
        if x1 < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif x1 == 0 or x1 == 1:
            return 1
        else:
            return x1 * Factorial.calc(x1 - 1)


# #
class Summary(RightOperator):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def calc(x1):
        return sum(int(digit) for digit in str(abs(x1)) if digit.isdigit())


# ~
class Tilda(LeftOperator):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def calc(x1):
        return -x1


# -
class MinusSign(LeftOperator):
    def __init__(self):
        super().__init__(7)

    @staticmethod
    def calc(x1):
        return -x1
