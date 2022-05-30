import unittest

from expressions.number import Number
from expressions.product import Product
from expressions.variable import Variable

class TestProduct(unittest.TestCase):

    def test_unique_variables_product_one_Variable(self):
        vars = Product(Variable("x"), Number(4)).unique_variables()
        self.assertEqual(vars, set("x"))

    def test_unique_variables_product_two_variables(self):
        vars = Product(Variable("x"), Variable("y")).unique_variables()
        self.assertEqual(vars, {"x", "y"})