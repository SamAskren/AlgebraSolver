from expressions.expression import Expression


class Equation:

    def __init__(self, lhs: Expression, rhs: Expression):
        self.lhs = lhs
        self.rhs = rhs

    def solve(self):
        pass

