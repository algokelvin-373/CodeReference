import sympy


def func_math(y_func, x_value):
    x = sympy.symbols('x')
    y = sympy.sympify(y_func)
    return y.subs(x, x_value)