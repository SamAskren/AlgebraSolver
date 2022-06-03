from expression import Expression


class Variable(Expression):
    def __init__(self, symbol):
        self.symbol = symbol

    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError(f"Variable {self.symbol} is not found")

    def unique_variables(self):
        return {self.symbol}


    def __repr__(self):
        return self.symbol


