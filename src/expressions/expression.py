import abc

class Expression(abc.ABC):
    @abc.abstractmethod
    def unique_variables(self):
        pass

    @abc.abstractmethod
    def evaluate(self, **bindings):
        pass

    @abc.abstractmethod
    def expand(self):
        pass

    # TODO

    # https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    # @abc.abstractmethod
    # def __eq__(self, other):
    #     pass

    @abc.abstractmethod
    def contains(self, var):
        pass

    # @abc.abstractmethod
    # def simplify(self):
    #     pass