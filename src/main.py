from expressions.apply import Apply
from expressions.function import Function
from expressions.number import Number
from expressions.power import Power
from expressions.product import Product
from expressions.sum import Sum
from expressions.variable import Variable
from expressions.quotient import Quotient
from expressions.difference import Difference
from expressions.negative import Negative
from expressions.sqrt import Sqrt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
                                    Product(Number(4), Product(Variable("a"), Variable("c"))))))),
                             Product(Number(2), Variable("a")))
    print(sq_expression)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
