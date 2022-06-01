import unittest

from expressions.number import Number

def test_unique_variables():
    exp = Number(4).unique_variables()
    assert exp == set()



