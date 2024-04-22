#!/usr/bin/env python3
"""
Module of 1-concurrent_coroutines
"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> Listi[float]:
    """ Multiple coroutines at the same time """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    for t in asyncio.as_completed(tasks):
        delay = await t
        delays.append(delay)
    return delays
