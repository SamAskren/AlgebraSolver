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
