from expressions.apply import Apply
from expressions.function import Function
from expressions.number import Number
from expressions.power import Power
from expressions.product import Product
from expressions.sum import Sum
from expressions.variable import Variable


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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
