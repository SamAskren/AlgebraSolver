from expressions.apply import Apply
from expressions.number import Number
from expressions.sum import Sum
from expressions.variable import Variable


def test_unique_variables_number():
    exp = Apply("sin", Number(4)).unique_variables()
    assert exp == set()


def test_unique_variables_sum():
    exp = Apply("sin", Sum(Variable("x"), Number(4))).unique_variables()
    assert exp == set("x")

