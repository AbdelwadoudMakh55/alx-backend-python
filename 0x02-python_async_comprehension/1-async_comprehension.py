#!/usr/bin/env python3
"""
Module: 1-async_comprehension
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async comprehension """
    return [rand async for rand in async_generator()]
