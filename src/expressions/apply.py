
class Apply():
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

    def unique_variables(self):
        return self.argument.unique_variables()

    def __repr__(self):
        return f"{self.function}({self.argument})"