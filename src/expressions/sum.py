
class Sum():

    def __init__(self, *exps):
        self.exps = exps

    def unique_variables(self):
        return set().union(*[exp.unique_variables() for exp in self.exps])

