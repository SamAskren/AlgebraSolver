import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def unique_variables(self):
        pass
    @abstractmethod
    def evaluate(self, **bindings):