from expressions.expression import Expression


class Function():
    def __init__(self, name):
        self.name = name

    def unique_variables(self):
        return set()

    def __repr__(self):
        return self.name

    def expand(self):
        return self
    
    def contains(self, value):
        return False