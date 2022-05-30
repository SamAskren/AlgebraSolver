import unittest

from expressions.apply import Apply
from expressions.number import Number
from expressions.sum import Sum
from expressions.variable import Variable

class TestApply(unittest.TestCase):

    def test_unique_variables_number(self):
        vars = Apply("sin", Number(4)).unique_variables()
        self.assertEqual(vars, set())

    def test_unique_variables_sum(self):
        vars = Apply("sin", Sum(Variable("x"), Number(4))).unique_variables()
        self.assertEqual(vars, set("x"))

