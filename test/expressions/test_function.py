import unittest

from expressions.function import Function

class TestFunction(unittest.TestCase):

    def test_unique_variables_function(self):
        vars = Function("sin").unique_variables()
        self.assertEquals(vars, set())


