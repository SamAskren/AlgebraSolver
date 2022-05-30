
class Product():
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def unique_variables(self):
        return self.exp1.unique_variables().union(self.exp2.unique_variables())


