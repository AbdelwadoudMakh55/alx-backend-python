#!/usr/bin/env python3
"""
Module of 102-type_checking
"""
from typing import List, Tuple, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Type Checking """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
        ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
