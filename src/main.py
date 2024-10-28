from expressions.apply import Apply
from expressions.function import Function
from expressions.number import Number
from expressions.operations import Power
from expressions.operations import Product
from expressions.operations import Sum
from expressions.variable import Variable
from expressions.operations import Quotient
from expressions.operations import Difference
from expressions.operations import Negative
from expressions.operations import Sqrt

def print_expressions():
    pf_expression = Product(Sum(Product(Number(3),
                                        Power(Variable("x"), Number(2))),
                                Variable("x")),
                            Apply(Function("sin"), Variable("x")))
    print(pf_expression)
    ln_expression = Apply(Function("ln"), Power(Variable("y"), Variable("z")))
    print(ln_expression)
    qu_expression = Quotient(Sum(Variable("a"), Variable("b")), Number(2))
    print(qu_expression)
    sb_expression = Difference(Power(Variable("b"), Number(2)),
                               Product(Number(4), Product(Variable("a"), Variable("c"))))
    print(sb_expression)
    n_expression = Negative(Sum(Power(Variable("x"), Number(2)), Variable("y")))
    print(n_expression)
    sq_expression = Quotient(Sum(Negative(Variable("b")), (Sqrt(Difference(Power(Variable("b"), Number(2)),
                                                                           Product(Number(4), Product(Variable("a"),
                                                                                                      Variable(
                                                                                                          "c"))))))),
                             Product(Number(2), Variable("a")))
    print(sq_expression)

def print_expand():
    Y = Variable('y')
    Z = Variable('z')
    A = Variable('a')
    B = Variable('b')
    prd_expression = Product(Sum(A, B), Sum(Y, Z))
    print(prd_expression.expand())

if __name__ == '__main__':
    print_expressions()
    print('------------------------------------------------')
    print_expand()