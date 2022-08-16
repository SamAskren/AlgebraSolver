import math

from expression import Expression


class Sqrt(Expression):
    def __init__(self, exp):
        self.exp = exp

    def evaluate(self, **bindings):
        return math.sqrt(self.exp.evaluate(**bindings))

    def unique_variables(self):
        return self.exp.unique_variables()

    def __repr__(self):
        return f"√({self.exp})"