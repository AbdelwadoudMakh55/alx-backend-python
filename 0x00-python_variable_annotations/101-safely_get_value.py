#!/usr/bin/env python3
"""
Module of 101-safely_get_value
"""
from typing import Any, Mapping, Optional, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[Optional[T]] = None) -> Union[Any,
                                                                  Optional[T]]:
    """ Type annotations """
    if key in dct:
        return dct[key]
    else:
        return default
