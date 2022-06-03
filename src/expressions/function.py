from expression import Expression


class Function(Expression):
    def __init__(self, name):
        self.name = name

    def unique_variables(self):
        return set()

    def __repr__(self):
        return self.name
