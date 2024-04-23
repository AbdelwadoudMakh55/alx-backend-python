#!/usr/bin/env python3
"""
Module: 0-async_generator
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """ async comprehension """
    for i in range(10):
        await asyncio.sleep(1)
        rand = random.uniform(0, 10)
        yield rand
