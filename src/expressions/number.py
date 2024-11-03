from expressions.expression import Expression


class Number(Expression):
    def __init__(self, number):
        self.number = number

    def evaluate(self, **bindings):
        return self.number

    def unique_variables(self):
        return set()

    def __repr__(self):
        return str(self.number)

    def expand(self):
        return self
    
    def contains(self, var):
        return False
    
    # def simplify(self):
    #     return self

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.number == other.number
        else:
            return False