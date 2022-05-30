from expressions.expressions import Apply, Function, Number, Power, Product, Sum, Variable, distinct_variables



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pf_expression = Product(Sum(Product(Number(3),
                                        Power(Variable("x"), Number(2))),
                                Variable("x")),
                            Apply(Function("sin"), Variable("x")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
