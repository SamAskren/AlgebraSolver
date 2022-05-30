
class Power():
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def unique_variables(self):
        return self.base.unique_variables().union(self.exponent.unique_variables())

    def __repr__(self):
        return f"{self.base}^{self.exponent}"