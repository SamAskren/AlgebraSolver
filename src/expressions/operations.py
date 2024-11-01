from expressions.expression import Expression
from expressions.number import Number
from expressions.variable import Variable
import math


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


class Difference(Expression):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def evaluate(self, **bindings):
        return self.exp1.evaluate(**bindings) - self.exp2.evaluate(**bindings)
    
    def unique_variables(self):
        return self.exp1.unique_variables().union(self.exp2.unique_variables())

    def __repr__(self):
        return f"({self.exp1} - {self.exp2})"
    
    def expand(self):
        return Difference(self.exp1.expand(), self.exp2.expand())

class Negative(Expression):

    def __init__(self, exp):
        self.exp = exp

    def evaluate(self, **bindings):
        return - self.exp.evaluate(**bindings)

    def unique_variables(self):
        return self.exp.unique_variables()

    def __repr__(self):
         return f"-{self.exp}"
    
    def expand(self):
        return Negative(self.exp.expand())

class Product(Expression):
    def __init__(self, exp1, exp2):
        if isinstance(exp2, Number) and (isinstance(exp1, Sum) or isinstance(exp1, Variable) or isinstance(exp2, Power)):
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


class Quotient(Expression):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self, **bindings):
        denomValue = self.denominator.evaluate(**bindings)
        if denomValue == 0:
            return float("nan")
        else:
            return self.numerator.evaluate(**bindings) / self.denominator.evaluate(**bindings)

    def unique_variables(self):
        return self.numerator.unique_variables().union(self.denominator.unique_variables())

    def __repr__(self):
        return f"{self.numerator} / {self.denominator}"
    
    def expand(self):
        expanded1 = self.exp1.expand()
        expanded2 = self.exp2.expand()
        if isinstance(expanded1, Sum):
            return Sum(*[Quotient(e, expanded2).expand()
                         for e in expanded1.exps])
        elif isinstance(expanded2, Sum):
            return Sum(*[Quotient(expanded1, e)
                         for e in expanded2.exps])
        else:
            return Quotient(expanded1, expanded2)

class Sqrt(Expression):
    def __init__(self, exp):
        self.exp = exp

    def evaluate(self, **bindings):
        return math.sqrt(self.exp.evaluate(**bindings))

    def unique_variables(self):
        return self.exp.unique_variables()

    def __repr__(self):
        return f"√({self.exp})"
    
    def expand(self):
        return Sqrt(self.exp.expand())

class Power(Expression):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def evaluate(self, **bindings):
        return self.base.evaluate(**bindings) ** self.exponent.evaluate(**bindings)

    def unique_variables(self):
        return self.base.unique_variables().union(self.exponent.unique_variables())

    def __repr__(self):
        return f"{self.base}^{self.exponent}"

    def expand(self):
        base_expanded = self.base.expand()
        if isinstance(base_expanded, Sum):
            base_copy = base_expanded.exps.clone()
            final_product = Product(base_copy[0].expand(), base_copy[1].expand())
            for val in base_copy[2:]:
                final_product = Product(final_product, val.expand())
            return final_product
        elif isinstance(base_expanded, Product):
            base_copy = base_expanded.exps.clone()
            final_product = Product(base_copy[0].expand(), base_copy[1].expand())
            return final_product
        else:
            return Power(base_expanded, self.exponent)

