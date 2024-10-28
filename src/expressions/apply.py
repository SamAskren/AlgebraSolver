import math

from expressions.expression import Expression


class Apply(Expression):
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

    def evaluate(self, **bindings):
        fn = None
        match self.function:
            case "sin":
                fn = math.sin
            case "cos":
                fn = math.cos
            case "tan":
                fn = math.tan
            case "ln":
                fn = math.log
            case "!":
                fn = math.factorial
            case "factorial":
                fn = math.factorial
            case "√":
                fn = math.sqrt
            case "sqrt":
                fn = math.sqrt

        return fn(self.argument.evaluate(**bindings))

    def unique_variables(self):
        return self.argument.unique_variables()

    def __repr__(self):
        return f"{self.function}({self.argument})"

    def expand(self):
        return Apply(self.function, self.argument.expand)