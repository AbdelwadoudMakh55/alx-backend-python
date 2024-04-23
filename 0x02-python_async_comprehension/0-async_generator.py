#!/usr/bin/env python3
"""
Module: 0-async_generator
"""
import asyncio
import random


async def async_generator() -> float:
    """ async comprehension """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
