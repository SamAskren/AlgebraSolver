
class Sqrt():
    def __init__(self, exp):
        self.exp = exp

    def unique_variables(self):
        return self.exp.unique_variables()

    def __repr__(self):
        return f"√({self.exp})"