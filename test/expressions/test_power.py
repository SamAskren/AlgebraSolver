import unittest

from expressions.power import Power
from expressions.number import Number
from expressions.sum import Sum
from expressions.variable import Variable

class TestPower(unittest.TestCase):

    def test_unique_variables_zero_variables(self):
        vars = Power(Number(3), Number(4)).unique_variables()
        self.assertEquals(vars, set())

    def test_unique_variables_one_variables(self):
        vars = Power(Variable("x"), Number(4)).unique_variables()
        self.assertEquals(vars, set("x"))

    def test_unique_variables_two_variables(self):
        vars = Power(Variable("x"), Variable("y")).unique_variables()
        self.assertEquals(vars, {"x", "y"})

