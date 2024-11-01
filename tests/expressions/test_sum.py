import unittest

from expressions.number import Number
from expressions.operations import Sum
from expressions.variable import Variable


def test_unique_variables_sum_one_variable():
    exp = Sum(Variable("x"), Number(4), Variable("x")).unique_variables()
    assert exp == set("x")


def test_unique_variables_sum_two_variables():
    exp = Sum(Variable("x"), Variable("y")).unique_variables()
    assert exp == {"x", "y"}

def test_evaluate_sum_two_numbers():
    exp = Sum(Number (20), Number (7)).evaluate()
    assert exp == 27

def test_evaluate_sum_three_numbers():
    exp = Sum(Number (2), Number (2), Number (7)).evaluate()
    assert exp == 11

def test_evaluate_sum_ten_numbers():
    exp = Sum(Number (3), Number (1), Number (4), Number (1), Number (5), Number (9), Number (2), Number (6), Number (5), Number (3)).evaluate()
    assert exp == 39