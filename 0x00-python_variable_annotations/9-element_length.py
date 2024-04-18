#!/usr/bin/env python3
"""
Module of 9-element_length
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Duck typing """
    return [(i, len(i)) for i in lst]
