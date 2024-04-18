#!/usr/bin/env python3
"""
Module of 7-to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ tuple """
    return (k, v**2)
