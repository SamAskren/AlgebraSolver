import unittest

from expressions.function import Function

def test_unique_variables_function():
    exp = Function("sin").unique_variables()
    assert exp == set()


