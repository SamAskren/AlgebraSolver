import unittest

from expressions.number import Number

class TestNumber(unittest.TestCase):

    def test_unique_variables(self):
        vars = Number(4).unique_variables()
        self.assertEquals(vars, set())



