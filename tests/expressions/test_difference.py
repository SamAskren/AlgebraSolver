import unittest

from expressions.number import Number
from expressions.operations import Difference
from expressions.variable import Variable


def test_unique_variables_difference_one_variable():
    exp = Difference(Variable("x"), Number(4)).unique_variables()
    assert exp == set("x")


def test_unique_variables_difference_two_variables():
    exp = Difference(Variable("x"), Variable("y")).unique_variables()
    assert exp == {"x", "y"}

def test_evaluate_difference_two_numbers():
    exp = Difference(Number (20), Number (7)).evaluate()
    assert exp == 13

def test_evaluate_difference_negative():
    exp = Difference(Number (7), Number (20)).evaluate()
    assert exp == -13