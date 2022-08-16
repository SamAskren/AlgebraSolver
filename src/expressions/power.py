from expression import Expression
from product import Product
from sum import Sum

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