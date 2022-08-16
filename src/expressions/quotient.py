from expression import Expression


class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self, **bindings):
        return self.numerator.evaluate(**bindings) / self.denominator.evaluate(**bindings)

    def unique_variables(self):
        return self.numerator.unique_variables().union(self.denominator.unique_variables())

    def __repr__(self):
        return f"{self.numerator} / {self.denominator}"
