import unittest

from expressions.number import Number
from expressions.sum import Sum
from expressions.variable import Variable


def test_unique_variables_sum_one_variable():
    exp = Sum(Variable("x"), Number(4), Variable("x")).unique_variables()
    assert exp == set("x")


def test_unique_variables_sum_two_variables():
    exp = Sum(Variable("x"), Variable("y")).unique_variables()
    assert exp == {"x", "y"}
