from expression import Expression


class Sum(Expression):

    def __init__(self, *exps):
        self.exps = exps

    def evaluate(self, **bindings):
        total = 0
        for val in self.exps:
            total += val.evaluate(**bindings)
        return total

    def unique_variables(self):
        return set().union(*[exp.unique_variables() for exp in self.exps])

    def __repr__(self):
        return f"({self.exps[0]} + {self.exps[1]})"

    def expand(self):
        return Sum(*[exp.expand() for exp in self.exps])