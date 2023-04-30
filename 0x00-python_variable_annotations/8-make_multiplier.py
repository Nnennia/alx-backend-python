#!/usr/bin/env python3
""" a type-annotated function make_multiplier that
takes a float multiplier as argument and returns
a function that multiplies a float by multiplier."""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply_float(n: float) -> float:
        """Returns product of multiplier and a number(n)"""
        return multiplier * n

    return multiply_float
