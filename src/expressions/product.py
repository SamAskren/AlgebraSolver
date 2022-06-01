from expressions.number import Number
from expressions.power import Power
from expressions.sum import Sum
from expressions.variable import Variable


class Product():
    def __init__(self, exp1, exp2):
        if isinstance(exp2, Number) and (isinstance(exp1, Sum) or isinstance(exp1, Variable) or isinstance( self.exp2, Power)):
            # swap the order if a variable or sum  is followed by a number
            self.exp1 = exp2
            self.exp2 = exp1
        else:
            self.exp1 = exp1
            self.exp2 = exp2

    def unique_variables(self):
        return self.exp1.unique_variables().union(self.exp2.unique_variables())

    def __repr__(self):
        if isinstance(self.exp1, Number) and \
                (isinstance(self.exp2, Sum) or isinstance(self.exp2, Variable) or isinstance( self.exp2, Power)):
            return f"{self.exp1}{self.exp2}"
        else:
            return f"{self.exp1} * {self.exp2}"
