import unittest
import math

from expressions.number import Number
from expressions.operations import Quotient
from expressions.variable import Variable

def test_unique_variables_quotient_one_Variable():
    exp = Quotient(Variable("x"), Number(4)).unique_variables()
    assert exp == set("x")

def test_unique_variables_quotient_two_variables():
    exp = Quotient(Variable("x"), Variable("y")).unique_variables()
    assert exp == {"x", "y"}

def test_evaluate_quotient():
    exp = Quotient(Number (4), Number (2)).evaluate()
    assert exp == 2

def test_evaluate_quotient_0():
    exp = Quotient(Number (4), Number (0)).evaluate()
    assert math.isnan(exp)