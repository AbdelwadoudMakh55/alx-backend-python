#!/usr/bin/env python3
"""
Module of 8-make_multiplier
"""
from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """  function that returns function """
    return lambda multiplier: multiplier * 2
