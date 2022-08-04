from pyparsing import lineStart
import sympy
import numpy as np
import matplotlib.pyplot as plt

xx = np.array([1, 2, 3, 4, 5])
yy = np.array([1, 1, 2, 6, 24])


def diff(m: float, n: float) -> float:
    if n - m == 1:
        return (yy[n] - yy[m]) / (xx[n] - xx[m])
    else:
        _diff = (diff(m + 1, n) - diff(m, n - 1)) / (xx[n] - xx[m])
        return _diff


x = sympy.Symbol('x')


def polynom(n: int) -> str:
    if n == 1:
        return (diff(0, 1) * (x - xx[0]))
    else:
        term = diff(0, n)
        for i in range(0, n):
            term *= (x - xx[i])
        print(term)
        ans = term + polynom(n - 1)
        return ans


print(sympy.simplify(polynom(4) + yy[0]))