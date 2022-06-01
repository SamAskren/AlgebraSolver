

class Variable():
    def __init__(self, symbol):
        self.symbol = symbol

    def unique_variables(self):
        return {self.symbol}


    def __repr__(self):
        return self.symbol
