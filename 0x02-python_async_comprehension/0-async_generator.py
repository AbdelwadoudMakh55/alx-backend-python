#!/usr/bin/env python3
"""
Module: 0-async_generator
"""
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """ async comprehension """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
