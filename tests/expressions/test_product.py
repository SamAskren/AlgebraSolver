import unittest

from expressions.number import Number
from expressions.operations import Product
from expressions.operations import Sum
from expressions.operations import Difference
from expressions.variable import Variable

def test_unique_variables_product_one_Variable():
    exp = Product(Variable("x"), Number(4)).unique_variables()
    assert exp == set("x")

def test_unique_variables_product_two_variables():
    exp = Product(Variable("x"), Variable("y")).unique_variables()
    assert exp == {"x", "y"}

def test_evaluate_product():
    exp = Product(Number(2), Number(7)).evaluate()
    assert exp == 14

def test_evaluate_product_sum():
    exp = Product(Sum(Number(2), Number(7)), Number(3)).evaluate()
    assert exp == 27

def test_evaluate_product_difference():
    exp = Sum(Product(Difference(Number(20), Number(7)), Number(2)), Number(1)).evaluate()
    assert exp == 27