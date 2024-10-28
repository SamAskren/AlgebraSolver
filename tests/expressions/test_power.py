import unittest

from expressions.operations import Power
from expressions.number import Number
from expressions.operations import Sum
from expressions.variable import Variable

def test_unique_variables_zero_variables():
    exp = Power(Number(3), Number(4)).unique_variables()
    assert exp == set()

def test_unique_variables_one_variables():
    exp = Power(Variable("x"), Number(4)).unique_variables()
    assert exp == set("x")

def test_unique_variables_two_variables():
    exp = Power(Variable("x"), Variable("y")).unique_variables()
    assert exp ==  {"x", "y"}

