from expression import Expression


class Number(Expression):
    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number

    def unique_variables(self):
        return set()

    def __repr__(self):
        return str(self.number)
