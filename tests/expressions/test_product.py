import unittest

from expressions.number import Number
from expressions.operations import Product
from expressions.variable import Variable

def test_unique_variables_product_one_Variable():
    exp = Product(Variable("x"), Number(4)).unique_variables()
    assert exp == set("x")

def test_unique_variables_product_two_variables():
    exp = Product(Variable("x"), Variable("y")).unique_variables()
    assert exp == {"x", "y"}