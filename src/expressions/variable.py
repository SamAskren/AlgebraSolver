from expressions.expression import Expression


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

    def expand(self):
        return self
    
    def contains(self, var):
        if self.symbol.contains(var):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.symbol == other.symbol
        else:
            return False