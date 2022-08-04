import matplotlib.pyplot as plt
import math as math
import numpy as np

def f(x: float) -> float:
    # y: float =
    # return y
    return 1

def df(x: float) ->float:
    # y: float = 
    # return y
    return 1


def newton(x0: float, error: float ) -> float:
    x: float = x0
    previous: float = 0
    while (abs(x - previous)) > error:
        previous = x
        x = previous - f(previous) / df(previous)
    return x

x0: float = 2.5

print(newton(x0, 10 ** -5))