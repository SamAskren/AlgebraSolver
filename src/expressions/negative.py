from expression import Expression


class Negative(Expression):

    def __init__(self, exp):
        self.exp = exp

    def evaluate(self, **bindings):
        return - self.exp.evaluate(**bindings)

    def unique_variables(self):
        return self.exp.unique_variables()

    def __repr__(self):
         return f"-{self.exp}"