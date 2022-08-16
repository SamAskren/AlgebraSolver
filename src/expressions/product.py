from expression import Expression
from expressions.number import Number
from expressions.power import Power
from expressions.sum import Sum
from expressions.variable import Variable


class Product(Expression):
    def __init__(self, exp1, exp2):
        if isinstance(exp2, Number) and (isinstance(exp1, Sum) or isinstance(exp1, Variable) or isinstance( self.exp2, Power)):
            # swap the order if a variable or sum  is followed by a number
            self.exp1 = exp2
            self.exp2 = exp1
        else:
            self.exp1 = exp1
            self.exp2 = exp2

    def evaluate(self, **bindings):
        return self.exp1.evaluate(**bindings) * self.exp2.evaluate(**bindings)

    def unique_variables(self):
        return self.exp1.unique_variables().union(self.exp2.unique_variables())

    def __repr__(self):
        if isinstance(self.exp1, Number) and \
                (isinstance(self.exp2, Sum) or isinstance(self.exp2, Variable) or isinstance( self.exp2, Power)):
            return f"{self.exp1}{self.exp2}"
        else:
            return f"{self.exp1} * {self.exp2}"

    def expand(self):
        expanded1 = self.exp1.expand()
        expanded2 = self.exp2.expand()
        if isinstance(expanded1, Sum):
            return Sum(*[Product(e, expanded2).expand()
                         for e in expanded1.exps])
        elif isinstance(expanded2, Sum):
            return Sum(*[Product(expanded1, e)
                         for e in expanded2.exps])
        else:
            return Product(expanded1, expanded2)