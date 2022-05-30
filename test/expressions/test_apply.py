import unittest

from expressions.apply import Apply
from expressions.number import Number
from expressions.sum import Sum
from expressions.variable import Variable

class TestNumber(unittest.TestCase):

    def test_unique_variables_number(self):
        vars = Apply("sin", Number(4)).unique_variables()
        self.assertEquals(vars, set())

    def test_unique_variables_sum(self):
        vars = Apply("sin", Sum(Variable("x"), Number(4))).unique_variables()
        self.assertEquals(vars, set("x"))

