import unittest

from expressions.number import Number
from expressions.sum import Sum
from expressions.variable import Variable

class TestSum(unittest.TestCase):

    def test_unique_variables_sum_one_Variable(self):
        vars = Sum(Variable("x"), Number(4), Variable("x")).unique_variables()
        self.assertEquals(vars, set("x"))


    def test_unique_variables_sum_two_variables(self):
        vars = Sum(Variable("x"), Variable("y")).unique_variables()
        self.assertEquals(vars, {"x", "y"})