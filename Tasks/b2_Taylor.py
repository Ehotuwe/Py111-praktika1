"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value

    """
    e=1
    a=1
    for i in range(1,100):
        a=a*i
        e=e+(x**i)/a
    return e


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    a=1
    b = 0
    for i in range (1, 20):
        a = (2 * i + 1) * 2 * i * a
        n = 2 * i + 1
        b = b+(-1) ** i * (x ** n) / a

    return x + b