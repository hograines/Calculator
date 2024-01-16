from math import pow


class Operator(object):
    def __init__(self, priority):
        self.priority = priority


class LeftOp(Operator):
    def __init__(self, priority):
        super().__init__(priority)


class RightOp(Operator):
    def __init__(self, priority):
        super().__init__(priority)


class BetweenOp(Operator):
    def __init__(self, priority):
        super().__init__(priority)


class Add(BetweenOp):
    def __init__(self):
        super().__init__(1)

    @staticmethod
    def calc(x1, x2):
        return x1+x2


class Sub(BetweenOp):
    def __init__(self):
        super().__init__(1)

    @staticmethod
    def calc(x1, x2):
        return x1-x2


class Mul(BetweenOp):
    def __init__(self):
        super().__init__(2)

    @staticmethod
    def calc(x1, x2):
        return x1 * x2


class Div(BetweenOp):
    def __init__(self):
        super().__init__(2)

    @staticmethod
    def calc(x1, x2):
        return x1 / x2


class Pow(BetweenOp):
    def __init__(self):
        super().__init__(3)

    @staticmethod
    def calc(x1, x2):
        return pow(x1, x2)


class Mod(BetweenOp):
    def __init__(self):
        super().__init__(4)

    @staticmethod
    def calc(x1, x2):
        return x1 % x2


class Avg(BetweenOp):
    def __init__(self):
        super().__init__(5)

    @staticmethod
    def calc(x1, x2):
        return (x1 + x2)/2


class Max(BetweenOp):
    def __init__(self):
        super().__init__(5)

    @staticmethod
    def calc(x1, x2):
        if x1 > x2:
            return x1
        return x2


class Min(BetweenOp):
    def __init__(self):
        super().__init__(5)

    @staticmethod
    def calc(x1, x2):
        if x1 < x2:
            return x1
        return x2


class Fact(RightOp):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def calc(x1):
        if x1 == 0 or x1 == 1:
            return 1
        else:
            return x1 * Fact.calc(x1 - 1)


class Sum(RightOp):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def calc(x1):
        return sum(int(digit) for digit in str(abs(x1)) if digit.isdigit())


class Tilda(LeftOp):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def calc(x1):
        return -x1
